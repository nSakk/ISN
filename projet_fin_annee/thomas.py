from datetime import *
import requests
from newsapi import *

ville = input("Entre la ville que tu veux : ")

r = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=ab0b9935472a05bf72192f5d3f36cb11&q={}&lang=fr".format(ville))
data=r.json()
t=data['main']['temp']
w=data['name']
weather=data['weather'][0]['description']
print("La ville est {}".format(w))
print("La témpérature est de {} degrés C".format(t-273.15))
print(weather)
print("#-------------------------------------------")
heure = datetime.now().time()
print(heure.hour, ':', heure.minute)
print("#-------------------------------------------")
print("Actu du jour")
newsapi = NewsApiClient(api_key='3dc1dd43f9914d8891b0c45875f34882')
data = all_articles = newsapi.get_everything(q='a',
                                      language='fr',
                                      domains='lemonde.fr,',
                                      sort_by='publishedAt',
                                      page=2)
a = 0
for loop in range(20):
    print(a+1, " ", data['articles'][a]['title'])
    print(data['articles'][a]['url'])
    a += 1

p = input("Appuiez sur entrée pour continuer")