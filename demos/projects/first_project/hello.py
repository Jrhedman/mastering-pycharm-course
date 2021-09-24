import requests
#https://weather.talkpython.fm/

resp = requests.get('https://weather.talkpython.fm/api/weather?city=waxhaw&state=nc&country=US&units=imperial')
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']
city = data['location']['city']
state = data['location']['state']

print(f"It's {temp}F outside in {city}, {state}.")
