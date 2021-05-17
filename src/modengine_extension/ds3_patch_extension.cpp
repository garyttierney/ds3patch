#include "ds3_patch_extension.h"

#include <thread>
#include <chrono>

std::thread startup_thread;

std::string DS3PatchExtension::id()
{
    return "ds3_patch";
}

void DS3PatchExtension::on_attach()
{
    using namespace std::chrono_literals;

    startup_thread = std::thread([&]() {
        void* steamclient = nullptr;

        do {
            std::this_thread::sleep_for(500ms);
            steamclient = GetModuleHandleW(L"steamclient64.dll");
        } while (steamclient == nullptr);

        p2p_manager->start();
    });
}

void DS3PatchExtension::on_detach()
{
    p2p_manager->stop();
}
