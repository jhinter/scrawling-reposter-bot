import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
from modules.scrape import fetch_articles, filter_articles
from modules.utils import get_new_session, persist_new_articles
from modules.post import post_new_articles

def main():
    session = get_new_session()
    search_queries = ["voi", "tier", "lime", "circ"]

    for search_query in search_queries:

        articles = fetch_articles(session, search_query)

        # custom filtering of articles
        filtered_articles = filter_articles(articles)

        # persisting article meta-data
        persist_new_articles(filtered_articles)

        # posting new articles on facebook page
        post_new_articles()

if __name__ == '__main__':
    while True:
        main()
        # 1 hour break
        time.sleep(60*60)

