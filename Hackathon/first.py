import requests
from bs4 import BeautifulSoup
  
URL = "https://www.mashina.kg/search/all/all/?currency=2&sort_by=upped_at+desc&time_created=all&page="
r = requests.get(URL)
  
soup = BeautifulSoup(r.text, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup())