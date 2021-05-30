import sqlite3
from flask import Flask, g
app = Flask(__name__)


DATABASE = './data/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


with app.app_context():
    @app.route('/')
    def hello_world():
        cur = get_db().cursor()
        return 'Hello, World!'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()