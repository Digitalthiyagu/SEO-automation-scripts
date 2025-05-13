import requests

def get_keywords_from_api(keyword):
    url = f"https://api.keywordtool.io/v2/search/keywords?apikey=YOUR_API_KEY&keyword={keyword}&country=us"
    response = requests.get(url)
    data = response.json()
    
    keywords = []
    for item in data.get('results', []):
        keywords.append(item['keyword'])
    
    return keywords

# Example usage:
main_keyword = 'SEO tools'
keywords = get_keywords_from_api(main_keyword)
print(f"Keywords related to '{main_keyword}':")
for keyword in keywords:
    print(keyword)
