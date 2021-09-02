import random
print("welcome to thew number guessing game")
print("I am guessing a number between 1 and 100")
choosen_number = random.randint(0, 100)
print(choosen_number)
#uncomment the above line and run to see whther test cases are getting passed
difficulty_level = input("choose a difficulty type easy or hard: ")
if difficulty_level == "easy":
    no_of_attempts = 10
elif difficulty_level == "hard":
    no_of_attempts = 5
else:
    print("invalid input")

is_game_over = False
while is_game_over != True:
    if no_of_attempts == 0:
        is_game_over = True
        print("you lost")
    else:
        print(f"you have {no_of_attempts} attempts to guess the number")
        user_input = int(input("make a guess: "))
        if user_input == choosen_number:
            is_game_over = True
            print("you found the right number")
        elif user_input > choosen_number:
            no_of_attempts -= 1
            print("too high")
        else:
            no_of_attempts -= 1
            print("too low")


