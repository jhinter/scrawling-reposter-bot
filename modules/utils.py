import requests
import pprint
from tinydb import TinyDB, Query

def get_new_session():
    session = requests.Session()
    return session

def get_db_table():
    db = TinyDB('./articles.json')
    table = db.table('posts')
    return table
    
def persist_new_articles(articles):
    table = get_db_table()
    for article in articles:
        if table.contains(Query().title == str(article["title"])) == False:
            table.insert({
                'title': article["title"],
                'description': article["description"],
                'link': article["link"],
                'sent': False
            })
            print('New article added: ' + article["title"])
        else:
            print('Article already exists: ' + article["title"])