import requests
from bs4 import BeautifulSoup

def extract_alt_tags(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        print(f"Image: {img.get('src')}, ALT: {img.get('alt')}")
        
extract_alt_tags("https://google.com")
