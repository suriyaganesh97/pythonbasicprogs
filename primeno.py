num1=int(input('enter a no'))
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