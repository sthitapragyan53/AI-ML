import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
import warnings

# Ignore warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# 1. Get the HTML content
response = requests.get(url)
html_data = response.text

# 2. Parse with BeautifulSoup (Needed for your StringIO step)
soup = BeautifulSoup(html_data, 'html.parser')

# 3. Use Pandas to read the table
# We convert the soup object to a string, then wrap it in StringIO
read_html_pandas_data = pd.read_html(StringIO(str(soup)))

# 4. Select the first table found
netflix_dataframe = read_html_pandas_data[0]

# Display the result
print(netflix_dataframe.head())