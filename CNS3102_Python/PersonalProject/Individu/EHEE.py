import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# print title
page_title = soup.title
print(page_title)

page_title = soup.title.text
print(page_title)

html = pd.read_html('https://toscrape.com/')
table1 = html[0]
print(table1)

print('\n')

# Example 1: Extracting data from a table into list 
table = soup.find('table', class_='table table-hover')
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    for column in columns:
        print(column.text)


# Example 1 too, but more nice output
table2 = soup.find('table', class_='table table-hover')
rows = table2.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    for i, column in enumerate(columns):
        if i == 0:
            print(column.text.ljust(30), end=' ')  # Left-aligned text for first column
        else:
            print(column.text.rjust(10), end=' ')  # Right-aligned text for other columns
    print()  # New line after each row