import requests
from bs4 import BeautifulSoup

def check_broken_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    broken_links = []
    for link in soup.find_all('a', href=True):
        link_url = link['href']
        if not link_url.startswith('http'):
            continue
        
        link_response = requests.head(link_url)
        if link_response.status_code != 200:
            broken_links.append((link_url, link_response.status_code))
    
    return broken_links

# Example usage:
url = 'https://trisul.org'
broken_links = check_broken_links(url)
if broken_links:
    print(f"Broken links on {url}:")
    for link, status in broken_links:
        print(f"{link} - Status Code: {status}")
else:
    print("No broken links found.")
