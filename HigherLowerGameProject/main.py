import random
from gameData import data
#print two random person initially followers store in variable
dict_1 = random.choice(data)

dict_1_follower_count = dict_1["follower_count"]
is_game_over = False
current_score = 0

while not is_game_over:
    dict_2 = random.choice(data)
    dict_2_follower_count = dict_2["follower_count"]
    print(f'A is {dict_1["name"]}, description is {dict_1["description"]}, country is {dict_1["country"]}')
    print(f'B is {dict_2["name"]}, description is {dict_2["description"]}, country is {dict_2["country"]}')
    # print statemnets for debugging
    print(dict_1_follower_count)
    print(dict_2_follower_count)
    user_guess = input("who do you think has high no of followers A or B: ")
    if user_guess == "A" or user_guess == "a":
        if dict_1_follower_count > dict_2_follower_count:
            print(f'yes you are right.{dict_1["name"]} has {dict_1_follower_count} followers and {dict_2["name"]} has only {dict_2_follower_count} followers')
            current_score += 1
        elif dict_2_follower_count > dict_1_follower_count:
            print(f'you are wrong.{dict_2["name"]} has {dict_2_follower_count} followers while {dict_1["name"]} has only {dict_1_follower_count} followers')
            print(f"your total score is {current_score}")
            is_game_over = True
        else:
            print(f'both have same no of {dict_1_follower_count} followers')
    elif user_guess == "B" or user_guess == "b":
        if dict_2_follower_count > dict_1_follower_count:
            print(f'yes you are right.{dict_2["name"]} has {dict_2_follower_count} followers and {dict_1["name"]} has only {dict_1_follower_count} followers')
            current_score += 1
            dict_1 = dict_2
        elif dict_1_follower_count > dict_2_follower_count:
            print(f'you are wrong.{dict_1["name"]} has {dict_1_follower_count} followers while {dict_2["name"]} has only {dict_2_follower_count} followers')
            print(f"your total score is {current_score}")
            is_game_over = True
        else:
            print(f'both have same no of {dict_1_follower_count} followers')
    else:
        print("invalid input")
        is_game_over = True
