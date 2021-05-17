#pragma once

#include "p2p_common.h"
#include "steam_bindings.h"

#include <concurrent_queue.h>
#include <atomic>


class P2PRecvWorker {
    friend class P2PSessionManager;

public:
    explicit P2PRecvWorker(SteamBindings* _steam)
        : steam(_steam)
    {
    }

    void run();

    void stop();

private:
    concurrency::concurrent_queue<P2PInboundMessage> queue;
    std::atomic_bool running;
    SteamBindings* steam;
};
