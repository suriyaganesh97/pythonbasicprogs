MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_is_running = True


def check_resources(user_given_data):
    """checks whether enough resources to make the coffee and returns if something is not enough"""
    is_enough_water = resources["water"] - MENU[user_given_data]["ingredients"]["water"]
    if user_given_data == "espresso":
        is_enough_milk = resources["milk"]
    else:
        is_enough_milk = resources["milk"] - MENU[user_given_data]["ingredients"]["milk"]
    is_enough_coffee = resources["coffee"] - MENU[user_given_data]["ingredients"]["coffee"]
    if is_enough_water <= 0:
        return "not enough water"
    elif is_enough_milk <= 0:
        return "not enough milk"
    elif is_enough_coffee <= 0:
        return "not enough coffee"
    else:
        return "enough resources"




def check_transaction(quart, dime, nick, pen, user_order_drink):
    total_value = float(quart*0.25 + dime*0.10 + nick*0.05 + pen*0.01)
    change = total_value - MENU[user_order_drink]["cost"]
    return change


def give_coffee(user_given_data):
    """reduces the resources and gives coffee to customer"""
    resources["water"] = resources["water"] - MENU[user_given_data]["ingredients"]["water"]
    if user_given_data == "espresso":
        resources["milk"] = resources["milk"]
    else:
        resources["milk"] = resources["milk"] - MENU[user_given_data]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[user_given_data]["ingredients"]["coffee"]
    return "enjoy your coffee"


# TODO Prompt user by asking “What would you like?
while machine_is_running:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    # TODO  Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        machine_is_running = False
    # TODO Print report.
    elif user_input == "report":
        print(f'water : {resources["water"]}')
        print(f'milk : {resources["milk"]}')
        print(f'coffee : {resources["coffee"]}')
    # TODO Check resources sufficient?
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        resource_check = check_resources(user_input)
        if resource_check == "not enough water" or resource_check == "not enough milk" or resource_check == "not enough coffee":
            print(resource_check)
            machine_is_running = False
        else:
            # TODO Process coins.
            print("Please insert coins")
            quarters = int(input("how many quarters? "))
            dimes = int(input("how many dimes? "))
            nickles = int(input("how many nickles? "))
            pennies = int(input("how many pennies? "))
            # TODO Check transaction successful
            balance_amount = check_transaction(quarters, dimes, nickles, pennies, user_input)
            if balance_amount >= 0:
                print(f"your balance amount is {balance_amount}")
                # TODO to reduce the resource and give coffee
                print(give_coffee(user_input))
            else:
                print("not enough money")
    else:
        print("invalid input")
        machine_is_running = False


