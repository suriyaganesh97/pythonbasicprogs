from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
options = menu.get_items()
while is_on:
    choice = input(f"what would you like {options} : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) #this drink is a menuitem object
        enough_resource = coffee_maker.is_resource_sufficient(drink)
        if enough_resource:
            is_payment_received = money_machine.make_payment(drink.cost)  # from menuitem object we are getting the cost of the drink
            if is_payment_received:
                coffee_maker.make_coffee(drink)












# coffee_object = CoffeeMaker()
# menu_object = Menu()
#
# money_machine = MoneyMachine()
# user_input = input(f"what would you like to have {menu_object.get_items()}  :").lower()
# if user_input == "report":
#     coffee_object.report()
#     money_machine.report()
# elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
#     menu_item_object = menu_object.find_drink(user_input)
#     is_resource_enough = coffee_object.is_resource_sufficient(menu_item_object)
#     if is_resource_enough:
#         money_object.process_coins()
#         money_object.make_payment(menu_list_object.cost)

