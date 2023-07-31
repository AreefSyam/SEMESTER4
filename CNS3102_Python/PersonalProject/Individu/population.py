import pandas as pd
html = pd.read_html('https://en.wikipedia.org/wiki/World_population')

# get the top 10 population table
table = html[4]

'''
The command df = html[4] is used to extract a specific table from the list of tables obtained from the HTML page.
When you use pd.read_html to read an HTML page, it returns a list of all the tables found on that page.
The index 4 in html[4] refers to the specific table you want to extract from the list.
Each table on the HTML page is represented as a separate DataFrame within the list. By specifying the index, you can select the desired table.
It's important to note that the index of the table may vary depending on the structure of the HTML page you're scraping.
In this case, html[4] was used assuming that the desired table is at index 4 within the list returned by pd.read_html.
If the structure of the HTML page changes, you may need to adjust the index accordingly to retrieve the correct table.
You can explore the list of tables returned by pd.read_html to determine the appropriate index for the table you want to extract.
You can print the list of tables (html) and inspect the tables to identify the one you need.
'''

# Retreive the required data from table
# ranking
rank = table.iloc[:,[0]].to_numpy().ravel()
# country
country = table.iloc[:,[1]].to_numpy().ravel()
# population
population = table.iloc[:,[2]].to_numpy().ravel()

# From data into matplotlib's pie
import matplotlib.pyplot as pp

# Plot the pie chart with labels
pp.pie(population, labels=country, autopct='%1.1f%%')
pp.title("World Population by Country")
pp.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
pp.show()

# Print the extracted data
print("Rank:", rank)
print("Country:", country)
print("Population:", population)