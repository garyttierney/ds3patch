#pragma once

#include "p2p_common.h"
#include "p2p_send_worker.h"
#include "p2p_recv_worker.h"
#include "steam_bindings.h"

#include <concurrent_queue.h>
#include <thread>
#include <set>

class P2PSessionManager {
    friend class DS3PatchExtension;
    friend class DS3PatchScripting;
public:
    P2PSessionManager()
        : steam()
        , recv_worker(&steam)
        , send_worker(&steam)
    {
    }

    bool accept_session_with_user(const CSteamID& user);

    bool close_session_with_user(const CSteamID& user);

    bool send_p2p_packet(const CSteamID& recipient, const char* source, uint32_t source_size, EP2PSend type);

    bool read_p2p_packet(char* buffer, uint32_t buffer_size, uint32_t* message_size, CSteamID* sender);

    bool is_p2p_packet_available(uint32_t* size);

    void start();

    void stop();

    std::set<CSteamID> updated_p2p_users;

private:
    SteamBindings steam;
    P2PSendWorker send_worker;
    P2PRecvWorker recv_worker;

    std::thread send_worker_thread;
    std::thread recv_worker_thread;
    std::set<CSteamID> active_peers;
    CSteamID current_lobby;

    STEAM_CALLBACK(P2PSessionManager, on_lobby_entered, LobbyEnter_t);
    STEAM_CALLBACK(P2PSessionManager, on_lobby_update, LobbyDataUpdate_t);
    STEAM_CALLBACK(P2PSessionManager, on_session_request, SteamNetworkingMessagesSessionRequest_t);
    STEAM_CALLBACK(P2PSessionManager, on_session_request_failed, SteamNetworkingMessagesSessionFailed_t);
};
