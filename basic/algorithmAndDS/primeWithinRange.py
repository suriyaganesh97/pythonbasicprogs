num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
for j in range(num1, num2 +1):
    if j > 1:
        for i in range(2, int(j/2) + 1):
            if j % i == 0:
                break
        else:
            print(j)
    else:
        pass