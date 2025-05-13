import requests
from bs4 import BeautifulSoup

def analyze_on_page_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.string if soup.title else 'No title'
    meta_desc = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
    meta_desc = meta_desc['content'] if meta_desc else 'No meta description'

    headers = []
    for header in ['h1', 'h2', 'h3']:
        headers.extend([h.get_text() for h in soup.find_all(header)])

    return title, meta_desc, headers

# Example usage:
url = 'https://example.com'
title, meta_desc, headers = analyze_on_page_seo(url)

print(f"Title: {title}")
print(f"Meta Description: {meta_desc}")
print("Headers:")
for header in headers:
    print(header)
