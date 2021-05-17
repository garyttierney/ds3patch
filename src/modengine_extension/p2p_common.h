#pragma once

#include <vector>

#include <steam/steam_api_common.h>
#include <steam/isteamnetworking.h>
#include <steam/isteamnetworkingmessages.h>

struct P2POutboundMessage {
    CSteamID recipient;
    EP2PSend type;
    std::vector<char> data;
};

struct P2PInboundMessage {
    CSteamID sender;
    std::vector<char> data;
};
