mylist = ['1','30','500','7','9','11','13','15','17']

#print(list(mylist[1] + mylist[2]))
print(list(mylist[1].split(' ')) + list(mylist[2].split(' ')))
mylist2 = mylist[1::2]
print(mylist2)
print(mylist[-1:-4:-1])