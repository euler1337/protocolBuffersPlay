#!/usr/bin/env python3
import sys
sys.path.insert(1, 'proto')
import addressbook_pb2
import requests as r


def main():
    address_book = addressbook_pb2.AddressBook()

    person = address_book.people.add()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.PhoneType.HOME

    url = "http://localhost:5000"

    response = r.post(url, address_book.SerializeToString())

    print("STATUS CODE: %d" % response.status_code)
    print("RESPONSE : \n" + response.text)

if __name__ == "__main__":
    main()