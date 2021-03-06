import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def fetch_articles(session, search_query):

    SEARCH_URL = 'https://www.mydealz.de/search'
    SEARCH_DATA = {'q': search_query}

    search_request = session.get(url=SEARCH_URL, params=SEARCH_DATA)
    response = BeautifulSoup(search_request.text, 'lxml')

    articles = response.select('article div.threadGrid')
    articles_objects = []

    for article in articles:

        title = article.select('div.threadGrid-title .thread-title a')[0]['title']
        description = article.select('div.cept-description-container')[0].text
        link = article.select('div.threadGrid-title .thread-title a')[0]['href']

        articles_objects.append({
            'title': title,
            'description': description,
            'link': link,
        })

    return articles_objects

def filter_articles(articles):

    # positive keywords, there has to be at least one
    RELEVANT_KEYWORDS = ['scooter']

    # negative keywords that aren't allowed
    IRRELEVANT_KEYWORDS = ['soda', 'juice']

    filtered_articles = []

    for article in articles:

        # making search case-insensitive
        title = article['title'].lower()
        relevant = False

        # check for positive keywords
        for keyword in RELEVANT_KEYWORDS:
            if title.find(keyword) != -1:
                relevant = True
                break

        # check for negative keywords
        if relevant == True:
            for keyword in IRRELEVANT_KEYWORDS:
                if title.find(keyword) != -1:
                    relevant = False
                    break

        # if at least 1 positive keyword and max. 0 negative keywords were found
        if relevant == True:
            filtered_articles.append(article)

    return filtered_articles
