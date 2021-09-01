import random
card_values = [11]
list_of_card_values = [11, 11]
sum_of_card_values = sum(list_of_card_values)
if sum_of_card_values > 21:
    for i in range(len(list_of_card_values)):
        print(list_of_card_values.remove(list_of_card_values[i]))