import http
from urllib.parse import urlparse, ParseResult
from typing import List

import requests
from bs4 import BeautifulSoup
from requests import Response
from api_tokens import MEDIASTACK_ACCESS_KEY
import urllib
from exceptions import InvalidArticleLink
import requests
import json
import openai

MAX_ARTICLEs_SUMMARY = 2
class ExtractedArticle:
    def __init__(self,url, article_summary: str):
        self.url = url
        self.article_summary = article_summary

async def get_latest_news() -> List[ExtractedArticle]:
    articles = []
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': MEDIASTACK_ACCESS_KEY,
        'sources' : 'cnn',
        'categories': '-general',
        'sort': 'published_desc',
        'limit': MAX_ARTICLEs_SUMMARY,
        })

    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode('utf-8')
    # Assume `decoded` contains the JSON response as a string
    response = json.loads(decoded)

    # Extract all the URLs from the response
    urls = [article['url'] for article in response['data']]

    # Print the URLs
    for i in range(min(len(urls), MAX_ARTICLEs_SUMMARY)):
        extracted_article = await summarise_link(urls[i])
        articles.append(extracted_article)

    return articles

async def summarise_link(url):
    article = await fetch_content(url)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot that summrize articles"},
                {"role": "user", "content": "summrize this article: " + article},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    return ExtractedArticle( url=url, article_summary=result)

async def fetch_content(url):
    parsed: ParseResult = urlparse(scheme="http", url=url)
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html.parser")
    # Get text from all <p> tags.
    p_tags = soup.find_all('p')
    # Get the text from each of the "p" tags and strip surrounding whitespace.
    p_tags_text = " ".join([tag.get_text().strip() for tag in p_tags])
    return p_tags_text
    