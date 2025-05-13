import requests

def get_keyword_ranking(keyword, domain):
    url = f"https://serpapi.com/search?q={keyword}&engine=google&api_key=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()

    for result in data.get('organic_results', []):
        if domain in result['url']:
            return result['position']
    
    return "Not ranked"

# Example usage:
keyword = 'best SEO tools'
domain = 'example.com'
position = get_keyword_ranking(keyword, domain)
print(f"Rank of '{keyword}' for {domain}: {position}")
