add_proto_library(addressbook_proto addressbook.proto)

add_executable(add_person add_person.cc)
target_link_libraries(add_person addressbook_proto)

add_executable(list_people list_people.cc)
target_link_libraries(list_people addressbook_proto)
