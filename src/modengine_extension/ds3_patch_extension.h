#pragma once

#include "p2p_session_manager.h"

#include <modengine/extension.h>
#include <lua.h>

using namespace modengine;

class DS3PatchExtension : public ModEngineExtension {
public:
    explicit DS3PatchExtension(ModEngineExtensionConnector* connector)
        : ModEngineExtension(connector)
    {
        p2p_manager = new P2PSessionManager();
    }

    virtual void on_attach();
    virtual void on_detach();
    virtual const char* id();

private:
    P2PSessionManager* p2p_manager;
    void bind_api();
};

extern "C" bool __declspec(dllexport) modengine_ext_init(ModEngineExtensionConnector* connector, ModEngineExtension** extension)
{
    *extension = new DS3PatchExtension(connector);
    return true;
}
