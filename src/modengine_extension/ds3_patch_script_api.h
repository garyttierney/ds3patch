#pragma once

#include "p2p_session_manager.h"

class DS3PatchScripting {
public:
    DS3PatchScripting(P2PSessionManager* session_manager_)
        : session_manager(session_manager_)
    {
    }

    auto get_peers()
    {
        auto matchmaking = session_manager->steam.matchmaking;
        auto user = session_manager->steam.user;
        auto lobby_member_count = matchmaking->GetNumLobbyMembers(session_manager->current_lobby);

        std::vector<CSteamID> lobby_members;
        if (lobby_member_count == 0) {
            return sol::as_table(lobby_members);
        }

        auto my_steamid = user->GetSteamID();
        for (auto i = 0; i < lobby_member_count; i++) {
            auto member = matchmaking->GetLobbyMemberByIndex(session_manager->current_lobby, i);
            if (member != my_steamid) {
                lobby_members.push_back(member);
            }
        }

        return sol::as_table(lobby_members);
    }

    auto get_peer_status(CSteamID& id)
    {
        SteamNetworkingQuickConnectionStatus status = {};
        SteamNetworkingIdentity identity = {};
        identity.SetSteamID(id);

        auto res = session_manager->steam.networking_messages->GetSessionConnectionInfo(identity, nullptr, &status);
        auto is_connected = res == k_ESteamNetworkingConnectionState_Connected;

        return std::make_tuple(is_connected, status);
    }

private:
    P2PSessionManager* session_manager;
};
