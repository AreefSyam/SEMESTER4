import pandas as pd
import numpy as np

# Plot the pie chart with labels
import matplotlib.pyplot as pp

# Read the HTML page and extract the table
html = pd.read_html('https://en.wikipedia.org/wiki/World_population')
table = html[4]

# Retrieve the required data from the table
rank = table.iloc[:, [0]].to_numpy().ravel()
country = table.iloc[:, [1]].to_numpy().ravel()
population = table.iloc[:, [2]].to_numpy().ravel()

# Create an array with the extracted data
data = np.column_stack((rank, country, population))

# Save the data to a CSV file
df = pd.DataFrame(data, columns=["Rank", "Country", "Population"])
df.to_csv("world_population.csv", index=False)

pp.pie(population, labels=country, autopct='%1.1f%%')
pp.title("World Population by Country")
pp.axis('equal')
pp.show()

# Print the extracted data
print("Rank:", rank)
print("Country:", country)
print("Population:", population)
