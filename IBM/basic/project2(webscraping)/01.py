import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "http://www.ibm.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the title of the page
    print("Page Title:", soup.title.string)
    
    # Find and print all paragraph texts
    print("\nAll paragraph texts:")
    for paragraph in soup.find_all('p'):
        print(paragraph.get_text())
        
    # Find and print all links
    print("\nAll links:")
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    