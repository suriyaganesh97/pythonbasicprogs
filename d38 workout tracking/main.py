import requests
import datetime
import time

APPLICATION_ID = "ad433866"
API_KEY = "fb2693a05520388d2175ab94b5887cac"
# sheety variables
SHEETY_ENDPOINT = "https://api.sheety.co/2284111d27793aa832a5e95e98265918/copyOfMyWorkouts/workouts"
params = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
}
BEARER_TOKEN = "fsdfdsfdsf3234dsvr434#sdvxfvbhdfbfghb"
Bearer_key = "Bearer "+BEARER_TOKEN
Bearer_header = {
    "Authorization": Bearer_key
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
Duration = response.json()['exercises'][0]['duration_min']
Exercise = response.json()['exercises'][0]['name']
Calories = response.json()['exercises'][0]['nf_calories']
print(Duration, Exercise, Calories)
current_date = datetime.datetime.now().strftime("%d/%m/%Y")
Date = current_date
curr_time = time.localtime()
Time = time.strftime("%H:%M:%S", curr_time)
sheety_json = {
    "workout": {
        "date": Date,
        "time": Time,
        "exercise": Exercise,
        "duration": Duration,
        "calories": Calories
    }
}
sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_json,headers=Bearer_header)
print(sheety_response.json())