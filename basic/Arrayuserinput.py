from array import *
arr=array('i',[])
arrlen=int(input('enter the length of the array  '))

for i in range(0,arrlen):
    x=int(input('enter the value  '))
    arr.append(x)
print(arr)