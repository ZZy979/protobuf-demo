proto_library(
    name = 'bar_proto',
    srcs = 'bar.proto',
    deps = '//foo:foo_proto',
    visibility = ['PUBLIC'],
)

cc_binary(
    name = 'mutable_caution',
    srcs = 'mutable_caution.cpp',
    deps = ':bar_proto',
)
