import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("choose 0 for rock, 1 for paper and 2 for scissors "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid choice")


print("computer \n")
computer_choice = random.randint(0, 2)    #generating computer random choice
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("Invalid choice")

if user_choice == computer_choice:
    print("draw ")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif user_choice == 1 and computer_choice == 0:
    print("you win")
elif user_choice == 2 and computer_choice == 1:
    print("you win")
else:
    print("computer wins")