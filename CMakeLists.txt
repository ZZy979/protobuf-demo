cmake_minimum_required(VERSION 3.18)
project(protobuf-demo)

set(CMAKE_CXX_STANDARD 17)

include(FetchContent)
include(protobuf.cmake)

include_directories(${CMAKE_SOURCE_DIR})
include_directories(${CMAKE_BINARY_DIR})

add_subdirectory(addressbook)
