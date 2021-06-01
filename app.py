import sqlite3
import click
from flask import Flask, current_app, g

from flask.cli import with_appcontext
app = Flask(__name__)

DATABASE = './data/database.db'
SCHEMA = './data/schema.sql'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

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
