#include "steam_bindings.h"

#include <filesystem>

namespace fs = std::filesystem;

SteamBindings::SteamBindings()
{


}

void SteamBindings::init()
{
    auto steam_client = GetModuleHandleW(L"steamclient64.dll");
    auto scanner = modengine::MemoryScanner(steam_client);
    auto interface_provider = scanner.find("\x89\x54\x24\x10\x89\x4C\x24\x08\x55\x53\x57\x41\x54\x41\x55\x41\x56\x41\x57\x48\x8B\xEC");

    if (!interface_provider) {
        throw std::runtime_error("Unable to find Steam interface provider");
    }

    auto steam_interface_provider = (GetSteamInterfacePointer) *interface_provider;

    this->networking_messages = (ISteamNetworkingMessages*)steam_interface_provider(1, 1, STEAMNETWORKINGMESSAGES_INTERFACE_VERSION, "NetworkingMessages");
    this->networking_utils = (ISteamNetworkingUtils*)steam_interface_provider(1, 1, STEAMNETWORKINGUTILS_INTERFACE_VERSION, "NetworkingUtils");
    this->matchmaking = (ISteamMatchmaking*)steam_interface_provider(1, 1, STEAMMATCHMAKING_INTERFACE_VERSION, "Matchmaking");
    this->utils = (ISteamUtils*)steam_interface_provider(1, 1, STEAMUTILS_INTERFACE_VERSION, "Utils");
}