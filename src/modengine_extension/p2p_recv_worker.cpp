#include "p2p_recv_worker.h"

const auto MAX_MESSAGES = 20;

void P2PRecvWorker::run()
{
    running = true;

    P2PInboundMessage current;
    SteamNetworkingMessage_t* messages = nullptr;

    while (running) {
        auto res = steam->networking_messages->ReceiveMessagesOnChannel(0, &messages, MAX_MESSAGES);

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
