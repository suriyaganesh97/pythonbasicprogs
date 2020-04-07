a=10
b=20
temp=a
a=b
b=temp
print(a,b)

a=10
b=20
a=a+b #without using third variable
b=a-b
a=a-b
print(a,b)

a=10
b=20
a=a^b #using xor gate
b=a^b
a=a^b
print(a,b)

a=10
b=20
a=a*b#using multiplication and division
b=a/b
a=a/b
print(a,b) #prints as float
print(int(a),int(b))

num1=20
num2=30
num1,num2=num2,num1  #swapping two numbers
print(num1,num2)


a,b,c=2,3,4
a,b,c=c,b,a
print(a,b,c)
