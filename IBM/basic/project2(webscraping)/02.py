# An international firm that is looking to expand its business
#  in different countries across the world has recruited you.
#  You have been hired as a junior Data Engineer and are tasked
#  with creating a script that can extract the list of the top 10 
# largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), 
# as logged by the International Monetary Fund (IMF).


url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
print(f"The URL for GDP data is: {url}")



import requests

# To bypass for bidden error, I will add a 'User-Agent' header to the request to simulate a browser request.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(f"Webpage status code with headers: {response.status_code}")

# Since the webpage was successfully retrieved (status code 200), I will now parse its HTML content using BeautifulSoup to prepare for data extraction. This will allow us to navigate and search within the HTML structure.


from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print("HTML content successfully parsed.")


#  Now that the HTML content is parsed, the next step is to locate the tables within the HTML, as GDP data is typically presented in tabular format. I will find all <table> tags in the soup object

tables = soup.find_all('table')
print(f"Found {len(tables)} tables on the page.")


# Since there are multiple tables,
#  I need to identify the correct table containing the GDP data. 
# I will inspect the first few tables to determine which one is relevant.
#  This often involves looking at table headers or the general structure.

gdp_table = None
for i, table in enumerate(tables):
    # A common heuristic is that the GDP table might have a specific class or many rows/columns
    # For this specific Wikipedia page, the GDP data is usually in the first or second table
    # Let's look for a table that contains 'GDP' or 'nominal' in its headers or content
    if 'GDP (nominal)' in table.get_text():
        gdp_table = table
        print(f"Found potential GDP table at index {i}")
        break

if gdp_table is None:
    # If the above heuristic doesn't work, we can print a summary of the first few tables
    # to visually inspect them. For this specific URL, the main table is usually the 3rd one.
    print("Could not find table by content, checking the table structure.")
    # Based on typical Wikipedia GDP pages, the relevant table is often the one with 3 or more columns and a good number of rows
    # Let's assume the relevant table is one of the larger ones. We can check the number of rows and columns.
    for i, table in enumerate(tables):
        rows = table.find_all('tr')
        if len(rows) > 10: # Assuming a table with GDP data will have many rows (countries)
            header_row = rows[0]
            headers = header_row.find_all(['th', 'td'])
            if len(headers) >= 3: # Assuming at least Country, Region, GDP columns
                if i == 2: # From visual inspection of typical Wikipedia GDP pages, it's often the 3rd table (index 2)
                    gdp_table = table
                    print(f"Identified GDP table at index {i} based on size and typical structure.")
                    break

if gdp_table is None:
    print("Could not identify the GDP table. Please inspect manually.")
else:
    print("GDP table successfully identified.")


# Now that the GDP table has been identified, I will extract its header row to understand the column names and prepare for data extraction.

if gdp_table:
    headers = [header.get_text(strip=True) for header in gdp_table.find_all('th')]
    print("Table Headers:", headers)
else:
    print("GDP table not found, cannot extract headers.")


# The previous attempt to extract headers resulted in an empty list, 
# indicating that the <th> tags might not be present or are not correctly identified in the table. 
# I will modify the header extraction logic to consider both <th> and <td> tags within the first row,
# as tables can sometimes use <td> for headers, especially in the first row. I will also print a snippet of the table to help in debugging if the issue persists


gdp_table = None
# Find tables with specific classes common for data tables on Wikipedia
# The main GDP table usually has classes 'wikitable' and 'sortable'
for i, table in enumerate(tables):
    if 'wikitable' in table.get('class', []) and 'sortable' in table.get('class', []):
        # Further check for typical GDP column headers in the first few rows
        first_row = table.find('tr')
        if first_row:
            headers_in_table = [header.get_text(strip=True) for header in first_row.find_all(['th', 'td'])]
            # Check if common GDP-related headers are present
            if any(key_word in ' '.join(headers_in_table) for key_word in ['Country/Territory', 'GDP (nominal)', 'Estimate']):
                gdp_table = table
                print(f"Identified GDP table at index {i} based on classes and header keywords.")
                break

if gdp_table is None:
    print("Could not identify the GDP table using 'wikitable sortable' classes or header keywords. Inspecting all tables might be necessary.")
else:
    print("GDP data table successfully identified.")



if gdp_table: 
    headers = [header.get_text(strip=True) for header in gdp_table.find_all('th')]
    print("Table Headers:", headers)
else:
    print("GDP table not found, cannot extract headers.")



data_rows = []
if gdp_table:
    for row in gdp_table.find_all('tr')[1:]: # Skip the header row
        cols = row.find_all(['td', 'th']) # Get all cells (td or th, just in case)
        cols = [ele.text.strip() for ele in cols]
        data_rows.append([ele for ele in cols if ele]) # Get rid of empty values
    
    print(f"Extracted {len(data_rows)} data rows.")
    print("First 5 data rows:", data_rows[:5])
else:
    print("GDP table not found, cannot extract data.")


import pandas as pd

if gdp_table and headers and data_rows:
    df_gdp = pd.DataFrame(data_rows, columns=headers)
    print("GDP DataFrame created successfully.")
    print(df_gdp.head())
else:
    print("Could not create DataFrame. Missing GDP table, headers, or data rows.")



import numpy as np

# Identify numerical columns based on the headers extracted
# Assuming the last three columns are the GDP estimates
numerical_cols = headers[1:]

for col in numerical_cols:
    # Remove commas and anything in brackets (e.g., [1])
    df_gdp[col] = df_gdp[col].str.replace(',', '', regex=False)
    df_gdp[col] = df_gdp[col].str.replace(r'\[.*\]', '', regex=True)
    
    # Convert to numeric, coercing errors to NaN
    df_gdp[col] = pd.to_numeric(df_gdp[col], errors='coerce')

print("Data types after cleaning and conversion:")
print(df_gdp.dtypes)
print("\nDataFrame head after cleaning numerical columns:")
print(df_gdp.head())



df_gdp = df_gdp.rename(columns={
    'Country/Territory': 'Country',
    'IMF(2026)[1]': 'GDP_IMF_2026',
    'World Bank(2024)[6]': 'GDP_WorldBank_2024',
    'United Nations(2024)[7]': 'GDP_UnitedNations_2024'
})

print("DataFrame columns renamed successfully.")
print(df_gdp.head())



df_top_10_gdp = df_gdp.sort_values(by='GDP_IMF_2026', ascending=False).head(10)
print("Top 10 economies by GDP (IMF 2026):")
print(df_top_10_gdp)




