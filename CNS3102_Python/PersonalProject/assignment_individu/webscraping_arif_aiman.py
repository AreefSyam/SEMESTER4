import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make a GET request to the URL
url = 'https://en.wikipedia.org/wiki/World_population'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the population data
table = soup.find_all('table')[4]
'''
The table element containing the population data is located
using soup.find_all('table')[4]. It assumes that the desired
tableis the fifth table on the page (index 4).
'''

# Extract the data from the table
rank_list = []
country_list = []
population_list = []

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    '''
    Within each row, the <td> elements (table cells)
    are found using row.find_all('td').
    '''
    if len(cols) >= 3:  # Check if there are enough columns
        '''
        to check if there are at least three columns (len(cols) >= 3)
        to ensure valid data is present.
        '''

        rank = row.th.get_text(strip=True)
        rank_list.append(rank)
        '''
        command get_text(strip=True) to remove any extra whitespace
        '''

        country = cols[0].get_text(strip=True)
        country_list.append(country)

        population_text = cols[1].get_text(strip=True).replace(',', '')
        population_list.append(population_text)
        ''' 
        to remove commas from the population values.
        '''

# Create an array with the extracted data
data = np.column_stack((rank_list, country_list, population_list))
'''
Using np.column_stack(), an array called data is created by combining the three lists.
'''

# Save the data to a CSV file
df = pd.DataFrame(data, columns=["Rank", "Country", "Population"])
df.to_csv("world_population.csv", index=False)

# Plot the pie chart with labels
plt.pie([float(p.strip('%')) for p in population_list], labels=country_list, autopct='%1.1f%%')
'''
Population values converted to floats and the Country names as labels.
The autopct='%1.1f%%' argument formats the percentage values in the pie chart.
'''
plt.title("World Population by Country")
plt.axis('equal')
plt.show()

# Print the extracted data
print("Rank:", rank_list)
print("Country:", country_list)
print("Population:", population_list)
