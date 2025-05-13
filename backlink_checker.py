import requests

def get_backlinks(domain):
    url = f"https://api.ahrefs.com/v3/site-explorer/backlinks?target={domain}&mode=domain"
    response = requests.get(url)
    data = response.json()

    backlinks = []
    for item in data.get('backlinks', []):
        backlinks.append(item['url_from'])
    
    return backlinks

# Example usage:
domain = 'example.com'
backlinks = get_backlinks(domain)
print(f"Backlinks for {domain}:")
for link in backlinks:
    print(link)
