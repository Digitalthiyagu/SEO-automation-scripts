from bs4 import BeautifulSoup
import requests

url = 'https://example.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.title.string.strip()
description = soup.find("meta", attrs={"name": "description"})

print("Title:", title)
print("Title Length:", len(title))
if description:
    desc = description["content"]
    print("Description:", desc)
    print("Description Length:", len(desc))
else:
    print("No description found.")
pt