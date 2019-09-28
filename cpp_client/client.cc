#include <iostream>
#include <fstream>
#include <string>
#include "proto/addressbook.pb.h"
using namespace std;



int main(int argc, char* argv[]) {
    GOOGLE_PROTOBUF_VERIFY_VERSION;

    tutorial::AddressBook address_book;
    /*
    tutorial::Person* person = address_book.add_people();
    person->set_id(1337);
    person->set_email("micke@tyson.com");
    person->set_name("Mr T");

    tutorial::Person::PhoneNumber* phone_number = person->add_phones();
    phone_number->set_number("0793474940494943");
    phone_number->set_type(tutorial::Person::MOBILE);

    std::cout << address_book.SerializeAsString << std::endl;

     google::protobuf::ShutdownProtobufLibrary();
*/
     return 0;

}
