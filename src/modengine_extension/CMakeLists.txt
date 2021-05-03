cmake_minimum_required(VERSION 3.19)
project(ds3patch)

find_package(ModEngine 2.0)
set(CMAKE_CXX_STANDARD 17)

add_library(ds3patch SHARED ds3_patch_extension.cpp ds3_patch_extension.h)
target_link_libraries(ds3patch modengine2)
