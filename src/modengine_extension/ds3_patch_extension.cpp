#include "ds3_patch_extension.h"

std::string DS3PatchExtension::id()
{
    return "ds3_patch";
}

void DS3PatchExtension::on_attach()
{
    p2p_manager->start();
}

void DS3PatchExtension::on_detach()
{
    p2p_manager->stop();
}

