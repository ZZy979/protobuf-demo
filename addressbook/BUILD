proto_library(
    name = 'addressbook_proto',
    srcs = 'addressbook.proto',
)

cc_binary(
    name = 'add_person',
    srcs = 'add_person.cc',
    deps = ':addressbook_proto',
)

cc_binary(
    name = 'list_people',
    srcs = 'list_people.cc',
    deps = ':addressbook_proto',
)
