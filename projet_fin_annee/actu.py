from newsapi import *
newsapi = NewsApiClient(api_key='3dc1dd43f9914d8891b0c45875f34882')

# /v2/everything
data = newsapi.get_everything(q='software', language='en', page_size=20)
print(data.keys())
print(data['articles'][0])

article = data['articles']
for x, y in enumerate(article):
    print(f'{x}    {y["title"]}')

for key, value in article[0].items():
    print(f"\n{key.ljust(15)}   {value}")

print(data[article][0]['url'])
print(data[article][0]['urlToImage'])