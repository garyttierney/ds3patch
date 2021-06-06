#include "p2p_session_manager.h"

#include <string>

#include <spdlog/spdlog.h>
#include <windows.h>

P2PSessionManager* global = nullptr;

const char* DS3PATCH_LOBBY_DATA_KEY = "ds3patch";
const char* DS3PATCH_LOBBY_DATA_VALUE = "1";

bool IsP2PPacketAvailable(ISteamNetworking*, uint32* pcubMsgSize, int iVirtualPort)
{
    return global->is_p2p_packet_available(pcubMsgSize);
}

bool SendP2PPacket(ISteamNetworking*, CSteamID steamIDRemote, const void* pubData, uint32 cubData, EP2PSend eP2PSendType, int)
{
    return global->send_p2p_packet(steamIDRemote, static_cast<const char*>(pubData), cubData, eP2PSendType);
}

bool ReadP2PPacket(ISteamNetworking* pThis, void* pubDest, uint32 cubDest, uint32* pcubMsgSize, CSteamID* psteamIDRemote, int)
{
    return global->read_p2p_packet(static_cast<char*>(pubDest), cubDest, pcubMsgSize, psteamIDRemote);
}

bool AcceptP2PSessionWithUser(CSteamID steamIDRemote)
{
    return global->accept_session_with_user(steamIDRemote);
}

bool CloseP2PSessionWithUser(CSteamID steamIDRemote)
{
    return global->close_session_with_user(steamIDRemote);
}

using namespace spdlog;

void P2PSessionManager::start()
{
    global = this;

    info("Started P2PSessionManager");

    steam.init();
    steam.utils->SetWarningMessageHook([](int severity, const char* text) {
        warn("Steam warning: {}", text);
    });

    steam.networking_utils->InitRelayNetworkAccess();
    steam.init();
    auto steam_api = GetModuleHandle("steam_api64.dll");
    auto steam_networking_provider = (decltype(&SteamNetworking))GetProcAddress(steam_api, "SteamNetworking");
    auto steam_networking = (uintptr_t*)steam_networking_provider();

    auto scanner = modengine::MemoryScanner(steam_api);
    if (!scanner.replace_at(*steam_networking, [](uintptr_t location) {
            auto vtable = (uintptr_t*)location;
            vtable[0] = (uintptr_t)&SendP2PPacket;
            vtable[1] = (uintptr_t)&IsP2PPacketAvailable;
            vtable[2] = (uintptr_t)&ReadP2PPacket;
            vtable[3] = (uintptr_t)&AcceptP2PSessionWithUser;
            vtable[4] = (uintptr_t)&CloseP2PSessionWithUser;
        })) {

        throw std::runtime_error("Failed to hook SteamNetworking");
    }

    recv_worker_thread = std::thread(&P2PRecvWorker::run, &recv_worker);
    send_worker_thread = std::thread(&P2PSendWorker::run, &send_worker);
}

void P2PSessionManager::stop()
{
    recv_worker.stop();
    send_worker.stop();
    recv_worker_thread.join();
    send_worker_thread.join();
}

void P2PSessionManager::on_lobby_entered(LobbyEnter_t* lobby)
{
    updated_p2p_users.clear();
    current_lobby.SetFromUint64(lobby->m_ulSteamIDLobby);

    info("Joined a lobby, flagging self as modern netcode client");

    // @todo: use this flag to send traffic to non-modded clients.
    steam.matchmaking->SetLobbyMemberData(lobby->m_ulSteamIDLobby, DS3PATCH_LOBBY_DATA_KEY, DS3PATCH_LOBBY_DATA_VALUE);
}

void P2PSessionManager::on_lobby_update(LobbyDataUpdate_t* lobby_data)
{
    if (lobby_data->m_ulSteamIDLobby == lobby_data->m_ulSteamIDMember) {
        return;
    }

    auto data = std::string(steam.matchmaking->GetLobbyMemberData(lobby_data->m_ulSteamIDLobby, lobby_data->m_ulSteamIDMember, DS3PATCH_LOBBY_DATA_KEY));
    if (data == DS3PATCH_LOBBY_DATA_VALUE) {
        info("Lobby member {:x} is also running modern netcode", lobby_data->m_ulSteamIDMember);
        updated_p2p_users.insert(lobby_data->m_ulSteamIDMember);
    }
}

struct SteamSurveillance;
auto surveillance_global = (struct SteamSurveillance*)0x14491b110;

using notify_session_request_ptr = void (*)(struct SteamSurveillance* surveillance, P2PSessionRequest_t* request);
auto notify_session_request = (notify_session_request_ptr)0x141959980;

void P2PSessionManager::on_session_request(SteamNetworkingMessagesSessionRequest_t* request)
{
    info("Received a session request from {:x}, accepting", request->m_identityRemote.GetSteamID().ConvertToUint64());

    P2PSessionRequest_t legacy_request = {};
    legacy_request.m_steamIDRemote = request->m_identityRemote.GetSteamID();

    notify_session_request(surveillance_global, &legacy_request);
}

void P2PSessionManager::on_session_request_failed(SteamNetworkingMessagesSessionFailed_t* request)
{
    error("{} {} {:x} {} {}", request->m_info.m_eEndReason, request->m_info.m_eState, request->m_info.m_identityRemote.GetSteamID64(), request->m_info.m_szConnectionDescription, request->m_info.m_szEndDebug);
}

bool P2PSessionManager::is_p2p_packet_available(uint32_t* size)
{
    if (recv_worker.queue.empty()) {
        return false;
    }

    *size = recv_worker.queue.unsafe_begin()->data.size();
    return true;
}

bool P2PSessionManager::read_p2p_packet(char* buffer, uint32_t buffer_size, uint32_t* message_size, CSteamID* sender)
{
    P2PInboundMessage message;
    if (!recv_worker.queue.try_pop(message)) {
        return false;
    }

    auto size = message.data.size();
    if (buffer_size < size) {
        return false;
    }

    std::copy(message.data.begin(), message.data.end(), buffer);
    *sender = message.sender;
    *message_size = size;

    return true;
}

bool P2PSessionManager::send_p2p_packet(const CSteamID& recipient, const char* source, uint32_t source_size, EP2PSend type)
{
    P2POutboundMessage message = {};
    message.recipient = recipient;
    message.data = std::vector(source, source + source_size);
    message.type = type;

    send_worker.queue.push(message);
    return true;
}

bool P2PSessionManager::accept_session_with_user(const CSteamID& user)
{
    SteamNetworkingIdentity id = {};
    id.SetSteamID(user);

    active_peers.insert(user);
    steam.networking_messages->AcceptSessionWithUser(id);
    return true;
}

bool P2PSessionManager::close_session_with_user(const CSteamID& user)
{
    SteamNetworkingIdentity id = {};
    id.SetSteamID(user);

    active_peers.erase(user);
    steam.networking_messages->CloseSessionWithUser(id);
    return true;
}
