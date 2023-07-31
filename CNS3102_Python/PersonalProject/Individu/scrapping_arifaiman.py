import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = 'https://books.toscrape.com/index.html'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information from the parsed HTML
    # For example, let's extract the titles, prices, and ratings of all books on the page
    book_titles = []
    book_prices = []
    book_ratings = []
    book_links = []
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        book_titles.append(title)

        price = book.find('p', class_='price_color').text
        book_prices.append(price)

        rating = book.p['class'][-1]
        book_ratings.append(rating)

        link = book.h3.a['href']
        book_links.append(link)

    # Save the data in a CSV file
    filename = 'book_data.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Price', 'Rating','Link'])  # Write the header row
        for title, price, rating, link in zip(book_titles, book_prices, book_ratings, book_links):
            writer.writerow([title, price, rating, link])

    print('Data saved successfully.')

else:
    print('Failed to retrieve the website content.')