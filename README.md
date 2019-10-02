# protocolBuffersPlay
Playing around with googles protocol buffers 

# Requirements: 
* Google Protocol Buffers: `https://developers.google.com/protocol-buffers/docs/tutorials`
* Plugin for golang generation: `https://developers.google.com/protocol-buffers/docs/reference/go-generated`
* Compiler/Environments to compile and run: C++, Python, Go, Rust.

# Generate Code
* For Python, C++ and Go : run `cd proto && ./generate.sh`
* Rust code is generated on the fly while building the project.

# Python 
Setup virtual environment: `source python_server/flask/venv/bin/activate`
Start server: `cd python_server/flask && ./runDev.sh`

# Compile C++ client
On a mac machine: `cd cpp_client && ./compile.sh`

