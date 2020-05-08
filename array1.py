from array import *
vals = array('i',[1,2,3,4,5])
vals.append(6)  #appedning a value to array
print(vals)  #printing the array
print()

newArr=array(vals.typecode,(a for a in vals))  #copying vals array to newArr array can be done with this single line fo code
print(newArr)

for i in range(len(vals)):  #using for loop to access the values in array
    print(vals[i])