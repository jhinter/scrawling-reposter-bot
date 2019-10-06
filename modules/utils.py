import requests
from tinydb import TinyDB, Query

def get_new_session():
    session = requests.Session()
    return session

def get_db_table():
    db = TinyDB('./articles.json')
    table = db.table('posts')
    return table
