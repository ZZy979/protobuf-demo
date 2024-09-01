FetchContent_Declare(
  protobuf
  GIT_REPOSITORY https://github.com/protocolbuffers/protobuf.git
  GIT_TAG v3.20.3
  SOURCE_SUBDIR cmake
)
set(protobuf_BUILD_TESTS OFF)
set(protobuf_BUILD_EXAMPLES OFF)
set(protobuf_WITH_ZLIB OFF)
FetchContent_MakeAvailable(protobuf)

#find_package(Protobuf REQUIRED)
include(FindProtobuf)

# 添加C++ proto库，用法：add_proto_library(<name> <source>)
function(add_proto_library name source)
  add_library(${name})
  protobuf_generate(
    TARGET ${name}
    LANGUAGE cpp
    PROTOC_OUT_DIR ${CMAKE_CURRENT_BINARY_DIR}
    PROTOS ${source}
  )
  target_link_libraries(${name} PUBLIC protobuf::libprotobuf)
  target_include_directories(${name} PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
endfunction()
