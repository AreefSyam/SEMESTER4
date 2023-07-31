import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/lessons/sign-up/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# print title
page_title = soup.title
print(page_title)

# print inside div
books_title = soup.find('table', attrs={'class': 'table table-hover'})
#\print(books_title)

# print link inside specific 'a'
ehe = soup.find('a', attrs={'class': 'gumroad-button'})
print(ehe.get('href'))

