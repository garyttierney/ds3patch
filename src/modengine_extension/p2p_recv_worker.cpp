#include "p2p_recv_worker.h"

#include <chrono>

const auto MAX_MESSAGES = 20;

void P2PRecvWorker::run()
{
    using namespace std::chrono_literals;

    running = true;

    P2PInboundMessage current;
    SteamNetworkingMessage_t* messages = nullptr;

    while (running) {
        auto res = steam->networking_messages->ReceiveMessagesOnChannel(0, &messages, MAX_MESSAGES);
        if (res == 0) {
            std::this_thread::yield();
            std::this_thread::sleep_for(5ms);
            continue;
        }

        for (auto i = 0; i < res; i++) {
            SteamNetworkingMessage_t* message = &messages[i];

            const char* data = (char*)message->GetData();
            current.data = std::vector(data, data + message->GetSize());
            current.sender = message->m_identityPeer.GetSteamID();

            queue.push(current);
            message->Release();
        }

        messages = nullptr;
    }
}

void P2PRecvWorker::stop()
{
    running = false;
}
