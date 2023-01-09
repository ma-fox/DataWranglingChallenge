import csv
import requests
from bs4 import BeautifulSoup

# Fetch the HTML page from Wikipedia
url = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe'

# Get the HTML page using the requests library
response = requests.get(url)

# Parse the HTML page using BeautifulSoup and the 'html.parser' parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element with the class 'wikitable' in the HTML docum
table = soup.find('table', attrs={'class': 'wikitable'})

# Extract the table data from the table element
tableData = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [element.text.strip() for element in cols]
    tableData.append([element for element in cols if element])

# Create a list of the columns to keep
columns_to_keep = [
    'Country', 'Year', 'Area', 'Population', 'GDP per capita',
    'Population density', 'Vehicle ownership', 'Total road deaths',
    'Road deaths per Million Inhabitants'
]

# Filter the table data to include only the desired columns
filtered_data = [[row[columns_to_keep.index(col)] for col in columns_to_keep]
                 for row in tableData[1:]]

# Sort the table data by the 'Road deaths per Million Inhabitants' column
filtered_data.sort(key=lambda x: float(x[columns_to_keep.index(
    'Road deaths per Million Inhabitants')]))

# Add a header row to the table data with the column names derived from the columns_to_keep list
filtered_data.insert(0, columns_to_keep)

# Write the table data to a CSV file called 'road_safety_facts_and_figures.csv'
with open('road_safety_facts_and_figures.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(filtered_data)
