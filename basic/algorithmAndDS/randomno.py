import random
num1 = int(input("enter starting limit: "))
num2 = int(input("enter ending limit: "))
for _ in range(10):
    print(random.randint(num1,num2),end=" ")