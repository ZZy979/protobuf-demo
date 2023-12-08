import sys

import addressbook_pb2


# This function fills in a Person message based on user input.
def prompt_for_address(person):
    person.id = int(input('Enter person ID number: '))
    person.name = input('Enter name: ')

    email = input('Enter email address (blank for none): ')
    if email:
        person.email = email

    while True:
        number = input('Enter a phone number (or leave blank to finish): ')
        if not number:
            break

        phone_number = person.phones.add()
        phone_number.number = number

        phone_type = input('Is this a mobile, home, or work phone? ')
        if phone_type == 'mobile':
            phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_MOBILE
        elif phone_type == 'home':
            phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_HOME
        elif phone_type == 'work':
            phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_WORK
        else:
            print('Unknown phone type. Using default.')


# Main procedure:  Reads the entire address book from a file,
# adds one person based on user input, then writes it back out to the same file.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} ADDRESS_BOOK_FILE')
        sys.exit(-1)

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    try:
        with open(sys.argv[1], 'rb') as f:
            address_book.ParseFromString(f.read())
    except IOError:
        print(f'{sys.argv[1]}: File not found. Creating a new file.')

    # Add an address.
    prompt_for_address(address_book.people.add())

    # Write the new address book back to disk.
    with open(sys.argv[1], 'wb') as f:
        f.write(address_book.SerializeToString())
