#datatypes
a=4.7
b=int(a) #type conversion
print(b)

c=3
d=float(c)
print(d)

k=complex(b,c)
print(k)

l=complex(0,b)
print(l)

m=complex(1,3)
print(m)

l=[10,20,30]#list
print(l)
print(type(l))

n={10,20,30,10}#set in set repeated values are not printed
print(n)
print(type(n))

o=[10,20,30]#tuple
print(o)
print(type(o))

num1=10
num2=20
print(num1>num2)#boolean returns false
print(num2>num1)#boolean returns false
num3=num1>num2#boolean datatype for num3
print(num3)
range(10) #converting range into list
print(list(range(10)))

s={1:'suriya',2:'rahul',3:'vijay'}
print(s)
print(s.keys())
print(s.values())
print(s[1])#to access value using key use square bracket
