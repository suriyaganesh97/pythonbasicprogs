import random

names = input("enter the names separated by a comma  ")
names = names.split(", ")

random_int = random.randint(0, len(names)-1)
print(f"{names[random_int]} should be paying the bill")