print("welcome to treasure island")
first_choice = input(" you want to go to left or right ").lower()
if first_choice == "right":
    print("game over ")
else:
    second_choice = input("you have come across a river , swim or wait for a boat ").lower()
    if second_choice == "swim":
        print("game over ")
    else:
        third_choice = input(" you have crossed safely, which one do you choose of three doors red,yellow and blue ").lower()
        if third_choice == "yellow":
            print("you have won the treasure ")
        else:
            print("game over")
