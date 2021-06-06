cmake_minimum_required(VERSION 3.18)
project(ds3patch)

find_package(ModEngine 2.0.1 REQUIRED)
add_library(steam_api SHARED IMPORTED)
set_target_properties(steam_api PROPERTIES
        IMPORTED_LOCATION "${STEAMWORKS_SDK}/redistributable_bin/win64/steam_api64.dll"
        IMPORTED_IMPLIB "${STEAMWORKS_SDK}/redistributable_bin/win64/steam_api64.lib"
        INTERFACE_INCLUDE_DIRECTORIES "${STEAMWORKS_SDK}/public")

add_library(ds3patch SHARED ds3_patch_extension.cpp p2p_send_worker.cpp p2p_session_manager.cpp p2p_recv_worker.cpp steam_bindings.cpp ds3_patch_script_api.cpp ds3_patch_script_api.h)

set(CMAKE_CXX_STANDARD 20)

target_link_libraries(ds3patch modengine2 steam_api)
