            # 'date_country_genre': item.find('div', 'b-content__inline_item-link').getText(),
            # 'entity': item.find('i', class_='entity'),
            # 'photo': 'https://rezka.ag' + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')

# https://rezka.aghttps://static.hdrezka.ac/i/2022/5/21/d67fe17b9f370nn77b92e.jpg\





import requests
from bs4 import BeautifulSoup

# URL = 'https://www.securitylab.ru/news/'
URL = 'https://rezka.ag/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 Edg/101.0.1210.53',

}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    films = []
    for item in items:
        films.append({
            'title': item.find('div', class_='b-content__inline_item-link').getText(),
            'entity': item.find('i', class_='entity').getText(),
            'link': item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            'photo': 'https://rezka.ag/' + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
        })
    return films
    # print(films)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for page in range(1,2):
            # html = get_html(f'{URL}page/{page}/')
            html = get_html(f'{URL}page/{page}/?filter=last')
            # https://rezka.ag/page/2/?filter=last
            films.extend(get_data(html.text))
        return films
    else:
        raise Exception('ERROR in parser!')

parser()