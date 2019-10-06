from tinydb import TinyDB, Query
import facebook
import utils

def post_new_articles():

    table = utils.get_db_table()

    for article in table.search(Query().sent == False):
        post = {
            'message': 'New deal!',
            'link': article.get('link'),
        }
        graph = facebook.GraphAPI(access_token='YOUR_TOKEN_HERE', version='3.1')
        
        api_request = graph.put_object(
            parent_object='YOUR_PAGE_HERE',
            connection_name='feed',
            message=post['message'],
            link=post['link']
        )

        if api_request == True:
            table.update({'sent': True}, Query().link == post['link'])
