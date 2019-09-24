#!/usr/bin/env bash

echo "Generating C++"
protoc -I=src --cpp_out=../cpp_client/proto src/addressbook.proto
echo "DONE!"

echo "Generating Python"
protoc -I=src --python_out=../python_server/proto src/addressbook.proto
echo "DONE!"

echo "Generating Go"
protoc -I=src --go_out=../go_server/proto src/addressbook.proto
echo "DONE!"