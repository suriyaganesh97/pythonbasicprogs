import json
test_dict = {"website": {"email": "suriyaganesh97@gmail.com", "password": "!tso9i3(%OYjt+"}}
with open('test1.json', 'w') as data_file:
    json.dump(test_dict, data_file)

    # import json
    #
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)