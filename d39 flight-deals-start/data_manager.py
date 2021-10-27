import requests
from pprint import pprint

SHEETY_URL = "https://api.sheety.co/2284111d27793aa832a5e95e98265918/copyOfFlightDeals/prices"


class DataManager:
    def __init__(self):
        pass

    # This class is responsible for talking to the Google Sheet.
    def data_sheet(self):
        response = requests.get(url=SHEETY_URL)
        pprint(response.json())
        return response.json()['prices']

    def data_sheet_update(self, i, code):
        print(i)
        print(code)
        id = 1
        id += 1
        sheety_json = {
            "price": {
                "id": id,
                "iataCode": code,
            }
        }
        update_response = requests.post(url=SHEETY_URL, json=sheety_json)
        print(update_response.json())
