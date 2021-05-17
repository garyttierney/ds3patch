#include "ds3_patch_extension.h"

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

void DS3PatchExtension::on_detach()
{
    p2p_manager->stop();
}
