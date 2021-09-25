#printing all perfect squares before 500
import math
for i in range(1,500):
    a=math.sqrt(i)  # all square roots will be found
    if i%a==0:  #to find prefect squares alone
        print(i,end=' ')  # to print with one space
