#!/usr/bin/env bash

# To lazy to create makefiles... (make sure to export PKG_CONFIG_PATH to point to restclient-cpp, protobuf for this to work.)
c++ client.cc proto/addressbook.pb.cc -o add_person_cpp.out -std=c++17 `pkg-config --cflags --libs protobuf restclient-cpp`
