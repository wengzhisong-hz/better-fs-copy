cmake_minimum_required(VERSION 3.21)
project(better_fs_copy)

set(CMAKE_CXX_STANDARD 14)

include_directories(node_modules/node-addon-api)
include_directories(node_modules/node-addon-api/external-napi)
include_directories(node_modules/node-addon-api/src)

add_executable(better_fs_copy
        node_modules/node-addon-api/external-napi/node_api.h
        node_modules/node-addon-api/src/node_api.cc
        node_modules/node-addon-api/src/node_api.h
        node_modules/node-addon-api/src/node_api_types.h
        node_modules/node-addon-api/src/node_internals.cc
        node_modules/node-addon-api/src/node_internals.h
        node_modules/node-addon-api/src/nothing.c
        node_modules/node-addon-api/src/util-inl.h
        node_modules/node-addon-api/src/util.h
        node_modules/node-addon-api/napi-inl.deprecated.h
        node_modules/node-addon-api/napi-inl.h
        node_modules/node-addon-api/napi.h
        src/better_fs_copy.cc)
