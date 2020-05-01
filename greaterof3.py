num1 = int(input('enter no 1  '))
num2 = int(input('enter no 2  '))
num3 = int(input('enter no 3  '))
if (num1 >= num2 and num1 >= num3):
    print('greater no is',num1)
if (num2 >= num3 and num2 >= num1):
    print('greater no is',num2)
if (num3 >= num1 and num3 >= num2):
    print('greater no is',num3)