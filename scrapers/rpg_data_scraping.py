import requests
from bs4 import BeautifulSoup as Bs


def what_is_rpg_text():
    url = 'https://bigenc.ru/c/komp-iuternaia-rolevaia-igra-5d8e86'
    response = requests.get(url)
    soup = Bs(response.text, 'html.parser')
    article_body = soup.find('div', class_='bre-article-body')
    elements = article_body.select('section > section > p')
    for element in elements:
        print(element.get_text())
        break
