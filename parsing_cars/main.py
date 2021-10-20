import requests
from bs4 import BeautifulSoup as BS

import csv 

def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_="catalog-list")
    cars = catalog.find_all('a', class_='catalog-list-item')
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = 'A car'

        try:
            img = car.find('img',class_='catalog-item-cover-img').get('src')
        except:
            img = 'https://stmartinblue.com/images/cars/default_car.jpg'

        try:
            price = car.find('span', class_ ='catalog-item-price').text.strip()
        except:
            price = 'договорная'
        data ={
            'title': title,
            'price': price,
            'img': img
        }
        write_to_csv(data)

def write_headers():
    with open('cars.csv', 'a') as file:
        field_names = ['название', 'цена', 'фото']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()




def write_to_csv(data):
    with open('cars.csv', 'a') as file:
        field_names = ['название', 'цена', 'фото']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow({'название': data['title'],'цена': data['price'],'фото': data['img']})
        

def main():
    with open('cars.csv', 'w') as file:pass
    write_headers()
    i =1
    while True:
        carsurl = f'https://cars.kg/offers/{i}?vendor=57fa24ee2860c45a2a2c0905'
        html = get_html(carsurl)
        catalog = BS(html, 'lxml').find('div', class_="catalog-list")
        if not catalog:
            break
        get_data(html)
        i  += 1
main()