proto_library(
    name = 'addressbook_proto',
    srcs = 'addressbook.proto',
)

cc_binary(
    name = 'write',
    srcs = 'write.cpp',
    deps = ':addressbook_proto',
)

cc_binary(
    name = 'read',
    srcs = 'read.cpp',
    deps = ':addressbook_proto',
)
