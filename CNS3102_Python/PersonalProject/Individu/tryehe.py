import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
links = soup.findAll('a')

for link in links:
    website = link.get('href')
    print(website)
