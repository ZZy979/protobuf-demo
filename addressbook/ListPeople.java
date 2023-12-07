package com.example.tutorial;

import com.example.tutorial.protos.AddressBookProtos.AddressBook;
import com.example.tutorial.protos.AddressBookProtos.Person;

import java.io.FileInputStream;

public class ListPeople {

    // Iterates though all people in the AddressBook and prints info about them.
    static void Print(AddressBook addressBook) {
        for (Person person : addressBook.getPeopleList()) {
            System.out.println("Person ID: " + person.getId());
            System.out.println("  Name: " + person.getName());
            if (person.hasEmail()) {
                System.out.println("  E-mail address: " + person.getEmail());
            }

            for (Person.PhoneNumber phoneNumber : person.getPhonesList()) {
                switch (phoneNumber.getType()) {
                    case PHONE_TYPE_MOBILE:
                        System.out.print("  Mobile phone #: ");
                        break;
                    case PHONE_TYPE_HOME:
                        System.out.print("  Home phone #: ");
                        break;
                    case PHONE_TYPE_WORK:
                        System.out.print("  Work phone #: ");
                        break;
                    default:
                        System.out.print("  Phone #: ");
                        break;
                }
                System.out.println(phoneNumber.getNumber());
            }
        }
    }

    // Main function: Reads the entire address book from a file and prints all
    // the information inside.
    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: ListPeople ADDRESS_BOOK_FILE");
            System.exit(1);
        }

        // Read the existing address book.
        AddressBook addressBook = AddressBook.parseFrom(new FileInputStream(args[0]));

        Print(addressBook);
    }
}
