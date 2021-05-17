#pragma once

#include <windows.h>

#include <steam/steam_api.h>
#include <modengine/util/memory_scanner.h>

typedef void* (*GetSteamInterfacePointer)(int, int, const char*, const char*);

class SteamBindings {
public:
    SteamBindings();

    ISteamNetworkingMessages* networking_messages;
    ISteamNetworkingUtils* networking_utils;
    ISteamMatchmaking* matchmaking;
};
