import requests
API_KEY = "1406ca9988396d7359e5cf0768401ed7"
LAT = 8.713913
LONG = 8.713913
parameters= {
"lat": LAT,
"lon" : LONG,
"appid" : API_KEY,
}

#https://api.openweathermap.org/data/2.5/onecall?lat=8.713913&lon=8.713913&appid=1406ca9988396d7359e5cf0768401ed7

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
hourly_forecast = response.json()["hourly"]
print(hourly_forecast)