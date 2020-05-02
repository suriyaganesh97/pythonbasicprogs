num=1
while num<=20:
    if(num%3!=0):
        if(num%5!=0):  #numbers not divisible by 3 and 5 gets printed
         print(num,end=' ')
    num=num+1
print('\n')
print('another way to exec the program')
#another way using continue statement
i=1
for i in range(1,21):
    if(i%3==0 or i%5==0):   #using or gate here
        continue           #by using continue we skip this iteration and continue wuth next one
    print(i,end=' ')
