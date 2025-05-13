import requests
from bs4 import BeautifulSoup

url = "https://google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Page Title:", soup.title.string)
