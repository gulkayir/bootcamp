
import requests
from bs4 import BeautifulSoup as BS

import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_site_parts(html):
    soup = BS(html, 'lxml')
    results = soup.find('div', class_="table-view-list")
    names = results.find_all('div', class_='list-item')
    for name in names:
        try:
            carnames = name.find('h2', class_='name').text.strip().replace(' ','')
        except:
            carnames = 'toyota'
        try:
            pic = name.find('img',class_='lazy-image').get('data-src')
        except:
            pic = 'https://t1-client.toyota-europe.com/images/toyota-logo.jpg'
        try:
            price = name.find('p', class_='price').text.strip().replace(' ','')
        except:
            price ='договорная'
        try:
            p1 = name.find('p',class_='year-miles').text.strip()
            p2 = name.find('p',class_='body-type').text.strip()
            p3 = name.find('p',class_='volume').text.strip()
            p4 = name.find('p',class_='city').text.strip()[0:6]
            shortinfo = p1+'\n'+p2+'\n'+p3+'\n'+p4
        except:
            shortinfo = 'нет информации'    
        
        data ={
            'carnames': carnames,
            'pic': pic,
            'price': price,
            'short info': shortinfo
        }
        to_the_csv(data)


def head():
    with open('mashina.csv', 'a') as file:
        field_names = ['название', 'фото', 'цена', 'краткая информация']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()


def to_the_csv(data):
    with open('mashina.csv', 'a') as file:
        field_names = ['название', 'фото', 'цена', 'краткая информация']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow({'название': data['carnames'],'фото': data['pic'], 'цена': data['price'],'краткая информация': data['short info']})
        


def main():
    with open('mashina.csv', 'w') as file:pass
    head()
    p = 1


    while True:
        mainurl = f'https://www.mashina.kg/search/toyota/all/?currency=2&region=6&sort_by=upped_at+desc&time_created=all&page={p}'
        html = get_html(mainurl)
        results = BS(html, 'lxml').find('div', class_="list-item")
        if not results:
            break
        get_site_parts(html)
        p  += 1
    # print(html)
main()

