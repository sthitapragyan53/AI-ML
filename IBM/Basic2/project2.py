import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# Step 1: Get the data
data = requests.get(url).text

# Step 2: Parse the HTML Data Using BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

# Corrected column names to match the dictionary inside the loop
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

# Step 3: Loop through rows
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    
    # Ensure the row actually has data
    if col:
        date = col[0].text
        Open = col[1].text
        high = col[2].text
        low = col[3].text
        close = col[4].text
        adj_close = col[5].text
        volume = col[6].text
        
        # Append to the DataFrame
        new_row = pd.DataFrame({
            "Date": [date], "Open": [Open], "High": [high], 
            "Low": [low], "Close": [close], "Adj Close": [adj_close], "Volume": [volume]
        })
        netflix_data = pd.concat([netflix_data, new_row], ignore_index=True)

print(netflix_data.head())