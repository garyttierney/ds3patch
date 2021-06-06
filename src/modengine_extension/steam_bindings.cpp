#include "steam_bindings.h"

#include <filesystem>

namespace fs = std::filesystem;

SteamBindings::SteamBindings()
{
}

void SteamBindings::init()
{
    auto steam_api = GetModuleHandle("steam_api64.dll");
    auto steam_client_provider = (decltype(&SteamClient))GetProcAddress(steam_api, "SteamClient");
    auto steam_client = steam_client_provider();
    auto steam_user = SteamAPI_GetHSteamUser();
    auto steam_pipe = SteamAPI_GetHSteamPipe();

    this->networking_utils = (ISteamNetworkingUtils*)steam_client->GetISteamGenericInterface(steam_user, steam_pipe, STEAMNETWORKINGUTILS_INTERFACE_VERSION);
    this->matchmaking = (ISteamMatchmaking*)steam_client->GetISteamGenericInterface(steam_user, steam_pipe, STEAMMATCHMAKING_INTERFACE_VERSION);
    this->utils = (ISteamUtils*)steam_client->GetISteamGenericInterface(steam_user, steam_pipe, STEAMUTILS_INTERFACE_VERSION);
    this->user = (ISteamUser*)steam_client->GetISteamGenericInterface(steam_user, steam_pipe, STEAMUSER_INTERFACE_VERSION);

    this->networking_messages = (ISteamNetworkingMessages*)steam_client->GetISteamGenericInterface(steam_user, steam_pipe,  STEAMNETWORKINGMESSAGES_INTERFACE_VERSION);
    this->networking_sockets = (ISteamNetworkingSockets*)steam_client->GetISteamGenericInterface(steam_user, steam_pipe,  STEAMNETWORKINGSOCKETS_INTERFACE_VERSION);
}
