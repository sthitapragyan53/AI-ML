# Install if needed
# !pip install requests
# !pip install beautifulsoup4
# !pip install html5lib

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Download webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text

# Step 2: Parse HTML
soup = BeautifulSoup(html_data, "html.parser")

# Step 3: Extract Tesla revenue table
tables = soup.find_all("table")
tesla_table = tables[1]

# Create empty DataFrame
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# Extract rows from table
for row in tesla_table.find_all("tr")[1:]:
    col = row.find_all("td")
    if len(col) == 2:
        date = col[0].text
        revenue = col[1].text
        tesla_revenue = pd.concat(
            [tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])],
            ignore_index=True
        )

# Step 4: Clean Revenue column
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(',|\$', "", regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(float)

# Step 5: Display last 5 rows
print(tesla_revenue.tail())