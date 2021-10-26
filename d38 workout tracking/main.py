import requests
APPLICATION_ID = "ad433866"
API_KEY = "fb2693a05520388d2175ab94b5887cac"
params = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
}
ENDPOINT_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_completed = input("type the exercise you did: ")
exercise = {
    "query": exercise_completed,
    "gender": "male",
    "weight_kg": 95,
    "height_cm": 167.64,
    "age": 22
}
response = requests.post(url=ENDPOINT_URL, json=exercise, headers=params)
print(response.json())