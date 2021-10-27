from data_manager import DataManager
from flight_search import FlightSearch
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.
data_manager = DataManager()
# sheet_data = data_manager.data_sheet()
# print(sheet_data)
sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]


flight_search = FlightSearch()
for i in range(0, len(sheet_data)):
    sheet_data[i]["iataCode"] = flight_search.get_IATA_CODE(sheet_data[i]['city'])
print(sheet_data)
for i in range(0, len(sheet_data)):
    data_manager.data_sheet_update(i, sheet_data[i]["iataCode"])


