#include "p2p_send_worker.h"

#include <chrono>
#include <thread>
#include <spdlog/spdlog.h>

void P2PSendWorker::run()
{
    using namespace std::chrono_literals;

    running = true;
    bool first = false;

    P2POutboundMessage curr = {};
    SteamNetworkingIdentity curr_recipient_id = {};

    while (running) {
        if (!queue.try_pop(curr)) {
            std::this_thread::yield();
            std::this_thread::sleep_for(5ms);
            continue;
        }

        int send_flags = k_nSteamNetworkingSend_AutoRestartBrokenSession;
        if (curr.type == k_EP2PSendUnreliable) {
            send_flags |= k_nSteamNetworkingSend_Unreliable;
        } else if (curr.type == k_EP2PSendUnreliableNoDelay) {
            send_flags |= k_nSteamNetworkingSend_UnreliableNoDelay;
        } else if (curr.type == k_EP2PSendReliable || curr.type == k_EP2PSendReliableWithBuffering) {
            send_flags |= k_nSteamNetworkingSend_Reliable;
        } else {
            send_flags |= k_nSteamNetworkingSend_Reliable;
        }

        curr_recipient_id.SetSteamID(curr.recipient);
        auto result = steam->networking_messages->SendMessageToUser(curr_recipient_id, &curr.data[0], curr.data.size(), send_flags, 0);
        if (result != k_EResultOK) {
            spdlog::error("Failed to send message to peer {:x}, reason: {}", curr.recipient.ConvertToUint64(), result);
        }

        curr_recipient_id.Clear();
    }
}

void P2PSendWorker::stop()
{
    running = false;
}
