print("welcome to pizza hut ")
size = input("what size of pizza you want, S, M or L ")
pepperoni = input("do you want pepperoni added Y or N ")
add_cheese = input("do you want cheese added or not ")
bill = 0
if size == 'S':
    bill += 15
if size == 'M':
    bill += 20
if size == 'L':
    bill += 25
if pepperoni == 'Y':
    bill += 2
if add_cheese == 'Y':
    bill += 2
print(f"The bill amount is {bill}")

