import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
# Wikipedia often has multiple tables; we want the main one
gdp_table = soup.find("table", class_="wikitable") 

# Extract all rows
rows = []
for row in gdp_table.find_all("tr"):
    cols = [td.text.strip() for td in row.find_all(["td", "th"])]
    if cols:
        rows.append(cols)

# Create DataFrame
df = pd.DataFrame(rows)

# --- FIX START ---
# Instead of naming columns, we take the 1st column (Country) 
# and the 3rd column (IMF Estimate) by index
df_gdp = df[[0, 2]].copy() 
df_gdp.columns = ["Country", "GDP_Raw"]

# Drop the header row if it was scraped as data
df_gdp = df_gdp[df_gdp["Country"] != "Country/Territory"]

# Clean the numbers: remove commas, footnotes, and non-numeric chars
df_gdp["GDP_Raw"] = df_gdp["GDP_Raw"].str.replace(r'[\s,\[\].*+]', '', regex=True)

# Convert to numeric
df_gdp["GDP (Billion USD)"] = pd.to_numeric(df_gdp["GDP_Raw"], errors="coerce")
# --- FIX END ---

# Sort and get top 10 (Wikipedia values are usually in Millions, so /1000 for Billions)
top_10 = df_gdp.dropna().sort_values("GDP (Billion USD)", ascending=False).head(10)

print(top_10[["Country", "GDP (Billion USD)"]])