#include "p2p_send_worker.h"

#include <chrono>
#include <thread>

void P2PSendWorker::run()
{
    using namespace std::chrono_literals;

    running = true;

    P2POutboundMessage curr;
    SteamNetworkingIdentity curr_recipient_id = {};

    while (running) {
        if (!queue.try_pop(curr)) {
            std::this_thread::yield();
            std::this_thread::sleep_for(5ms);
            continue;
        }

        int send_flags = k_nSteamNetworkingSend_AutoRestartBrokenSession;
        if ((curr.type & k_EP2PSendReliable) != 0) {
            send_flags |= k_nSteamNetworkingSend_Reliable;
        } else if ((curr.type & k_EP2PSendUnreliable) != 0) {
            send_flags |= k_nSteamNetworkingSend_Unreliable;
        }

        curr_recipient_id.SetSteamID(curr.recipient);
        steam->networking_messages->SendMessageToUser(curr_recipient_id, &curr.data[0], curr.data.size(), send_flags, 0);

        // @todo: handle k_EResultLimitExceeded: too much data queued.
    }
}

void P2PSendWorker::stop()
{
    running = false;
}
