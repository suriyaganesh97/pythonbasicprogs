a = int(input("enter a number"))
print(a)

if(a==5):  #should use colon at end
    print('five')  #block is based on indentation
if(a==7):
    print('seven')
else:
    print('not seven')

if a==1:  #can be used wihout open braces also
    print('one')

b=int(input('enter another no'))
if(b==3):
    print('three')
elif(b!=3):  #elif means else if
    print('not three')