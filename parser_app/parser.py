import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.mashina.kg/'

HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

#start
@csrf_exempt
def get_html(url, params=''):
    request = requests.get(url,headers=HEADER,params=params)
    return request

#get data
@csrf_exempt
def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')
    items = bs.find_all('div', class_='list-item list-label')
    list = []
    for item in items:
        list.append({
            'title' : item.find('div', class_='block title').get_text(),
            'price' : item.find('div', class_='block price').get_text(),
            'description' : item.find('div', class_='block info-wrapper item-info-wrapper').get_text(),
            'image' : URL + item.find('div', class_='image-wrap').find('img').get('src'),
        })
    return list

#parsing
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        list_items = []
        for page in range(0,1):
            html = get_html(f'https://www.mashina.kg/', params=page)
            list_items.extend(get_data(html.text))
        return list_items
    else:
        raise Exception('error in parse')

print(parser())

