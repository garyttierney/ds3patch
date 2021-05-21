#pragma once

#include <windows.h>

#include <steam/steam_api.h>
#include <modengine/util/memory_scanner.h>

typedef void* (*GetSteamInterfacePointer)(int, int, const char*, const char*);

class SteamBindings {
private:
    GetSteamInterfacePointer steam_interface_provider;
public:
    SteamBindings();

    ISteamNetworkingMessages* networking_messages;
    ISteamNetworkingSockets* networking_sockets;
    ISteamNetworkingUtils* networking_utils;
    ISteamMatchmaking* matchmaking;
    ISteamUtils* utils;
    ISteamUser* user;
    bool host = false;

    void init();

    void init_net_bindings();
};
