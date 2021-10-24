import requests
API_KEY = "1406ca9988396d7359e5cf0768401ed7"
LAT = 8.713913
LONG = 8.713913
parameters= {
"lat": LAT,
"lon" : LONG,
"appid" : API_KEY,
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
for i in range(0,13):
    hourly_forecast = response.json()["hourly"][i]["weather"][0]["id"]
    if hourly_forecast < 800:
        print(f"get umbrella for {i}th hour")
    else:
        print("no need for umbrella")
#hourly_forecast = response.json()["hourly"]
#print(hourly_forecast)