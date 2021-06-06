from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson import json_util
import os

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def get_users():
    users = list(mongo.db.users.find())
    return json_util.dumps(users)
