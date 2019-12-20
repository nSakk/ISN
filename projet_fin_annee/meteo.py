import requests

r = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=ab0b9935472a05bf72192f5d3f36cb11&q={}&lang=fr".format(ville))
data=r.json()
t=data['main']['temp']
w=data['name']
weather=data['weather'][0]['description']
print("La ville est {}".format(w))
print("La témpérature est de {} degrés C".format(t-273.15))
print(weather)