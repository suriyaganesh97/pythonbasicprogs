num1=int(input('enter a no'))
num2=num1
i=2
flag=0
while(i<num1):
    if(num1%i==0):
        flag+=1
    i+=1
if(flag==0):
    print('the no is prime number')
else:
    print('the no is not a prime number')


print()
print('more efficient way in below program')
for j in range(2,num1):      #can reduce the iteartion to num1/2 or square root of num1
    if(num1%j==0):
        print('not a prime no')
        break
else:    #using for else condition here
    print('the no is a prime no')


