import sqlite3
from flask import Flask, g

app = Flask(__name__)

DATABASE = './data/database.db'
SCHEMA = './data/schema.sql'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello_world():
    with app.app_context():
        cur = get_db().cursor()
        return 'Hello, World!'

@app.route('/init')
def init_app():
    init_db()
    return 'Database iniciated'
