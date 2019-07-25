from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS,cross_origin
import json


client = MongoClient('localhost:27017')
db = client.ContactDB

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/add_contact", methods = ['POST'])
@cross_origin(supports_credentials=True)
def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = db.Contacts.insert_one({
                "name" : user_name,
                "contact" : user_contact
            })
        return dumps({'message' : 'SUCCESS'})
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/get_all_contact", methods = ['GET'])
def get_all_contact():
    try:
        contacts = db.Contacts.find()
        return dumps(contacts)
    except Exception as e:
        return dumps({'error' : str(e)})
