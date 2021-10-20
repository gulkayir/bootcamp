# import requests
# from bs4 import BeautifulSoup

# def get_html(url):
#     response = requests.get(url)
#     print(response.status_code)


# def main():
#     nootebooks_url = 'https://www.eldorado.ru/c/noutbuki/'
#     pages = '?page='
#     get_html(nootebooks_url)
# main()

# import requests
# from bs4 import BeautifulSoup

# url = 'http://www.example.com/'
# r = requests.get(url)
# soup = BeautifulSoup(url, 'lxml')

# def getTitle():
#     if soup:
#         pageh1 = soup.find('h1')
#         print(pageh1)
#     else:
#         print("Title could not be found")
# getTitle()

# from bs4 import BeautifulSoup
# import requests

# b  = requests.get('https://www.makers.kg/')
# soup = BeautifulSoup(b.text, "lxml")

# images = soup.find_all('img')

# for img in images:
#     if img.has_attr('src') :
#         print('https://www.makers.kg/' + img['src'])

# from bs4 import BeautifulSoup
# import requests

# b  = requests.get('https://www.makers.kg/')
# soup = BeautifulSoup(b.text, "lxml")
# caption = soup.find_all('div',{'class':'feature-cards-card-info-subtitle'})
# for cap in caption:
#     print(cap.get_text())

        



# import requests
# from bs4 import BeautifulSoup


# html_text = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(html_text, 'lxml')
# all_ = soup.find_all('div', class_="feature-cards-card-info-subtitle")
# for i in all_:
# print(i.text)


# task5
# import requests
# from bs4 import BeautifulSoup


# html_text = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(html_text, 'lxml')
# all_ = soup.find_all('h3', class_="feature-cards-card-info-title")
# for i in all_:
#     print(i.text)




import requests
from bs4 import BeautifulSoup


def get_info(url):
    list_ = []
    html_text = requests.get('https://www.makers.kg').text
    soup = BeautifulSoup(html_text, 'lxml')
    all_ = soup.find_all('h3', class_ = "feature-cards-card-info-title")
    for i in all_:
        dict_ = {'name':i.text}
        list_.append(dict_)

        html_text = requests.get('https://www.makers.kg').text
        soup = BeautifulSoup(html_text, 'lxml')
        all_ = soup.find_all('div', class_="feature-cards-card-info-subtitle")
        f = 0
    for i in all_:
        list_[f]['description'] = i.text
        f += 1
                
        html_text = requests.get('https://www.makers.kg').text
        soup = BeautifulSoup(html_text, 'lxml')
        all_ = soup.find_all('img', class_ = "feature-cards-card-image")
        k = 0
        for i in all_:
            i = "https://www.makers.kg" +i.get('src').replace('.','',1)
            list_[k]['image_link'] = i
            k += 1
                    

            return list_


print(get_info('https://www.makers.kg'))



import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://enter.kg/').text
soup = BeautifulSoup(html_text, 'lxml')
li = soup.find_all('li', class_ = "VmClose")
category_list = [i.find('a').text for i in li if i.find('a')]
category_list = [i.text.strip() for i in li]
def find_category(categories, keyword):
    return [item for item in categories if keyword.lower() in item.lower()]
    print((find_category(category_list, 'Ноутбуки')))
print(category_list)



import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://www.imdb.com/chart/top').text
soup = BeautifulSoup(html_text, 'lxml')
title_list = soup.find_all('td', class_ = "titleColumn")

def get_link(title_list, name):
    for title_ in title_list:
        if name.lower() in title_.find("a").text.lower():
            return'https://www.imdb.com' + title_.find("a").get("href")

print(get_link(title_list, 'shawshank'))


