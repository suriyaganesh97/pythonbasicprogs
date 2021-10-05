import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # will raise exception if api issue
print(response)  # will give back response object
print(response.json())  # will give response as json format
latitude = response.json()["iss_position"]["latitude"]  #working with json same as dict in python
print(latitude)
longitude = response.json()["iss_position"]["longitude"]
print(longitude)