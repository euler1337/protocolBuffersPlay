from flask import Flask
from flask import jsonify
from flask import request
import sys
sys.path.insert(1, '../proto')
import addressbook_pb2

app = Flask(__name__)
 
@app.route('/', methods=['POST'])
def index():

    print("RAW DATA: ")
    print(request.get_data())

    address_book = addressbook_pb2.AddressBook()
    address_book.ParseFromString(request.get_data())
    print("PRETTY DATA:")
    print(address_book)

    return request.get_data()