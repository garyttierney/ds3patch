#include "ds3_patch_extension.h"
#include "ds3_patch_script_api.h"

#include <thread>
#include <chrono>

std::thread startup_thread;

const char* DS3PatchExtension::id()
{
    return "ds3_patch";
}

void DS3PatchExtension::on_attach()
{
    using namespace std::chrono_literals;
    using clock = std::chrono::steady_clock;

    bind_api();

    startup_thread = std::thread([&]() {
        auto start = clock::now();
        auto initialized = false;

        while ((clock::now() - start) < 15s && !initialized) {
            std::this_thread::sleep_for(500ms);

            auto steamclient_handle = GetModuleHandleW(L"steamclient64.dll");
            if (steamclient_handle == nullptr) {
                continue;
            }

            auto steampipe_initialized = !!SteamAPI_GetHSteamUser() && !!SteamAPI_GetHSteamPipe();
            if (steampipe_initialized) {
                initialized = true;
                break;
            }
        }

        if (initialized) {
            p2p_manager->start();
        }
    });
}

void DS3PatchExtension::bind_api()
{
    auto state = lua();
    auto ds3patch = state.create_named_table("DS3Patch");

    ds3patch.new_usertype<CSteamID>("CSteamID",
        "id", &CSteamID::ConvertToUint64);

    ds3patch.new_usertype<SteamNetworkingQuickConnectionStatus>("ConnectionStatus",
        "ping", &SteamNetworkingQuickConnectionStatus::m_nPing,
        "quality_local", &SteamNetworkingQuickConnectionStatus::m_flConnectionQualityLocal,
        "quality_remote", &SteamNetworkingQuickConnectionStatus::m_flConnectionQualityRemote,
        "send_delay", &SteamNetworkingQuickConnectionStatus::m_usecQueueTime);

    DS3PatchScripting scripting(p2p_manager);

    ds3patch.set_function("get_peers", &DS3PatchScripting::get_peers, scripting);
    ds3patch.set_function("get_peer_status", &DS3PatchScripting::get_peer_status, scripting);
}

void DS3PatchExtension::on_detach()
{
    p2p_manager->stop();
}
