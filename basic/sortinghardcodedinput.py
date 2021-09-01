from array import *
vals=array('i',[12,45,32,16,59,78,26])
#sorting in ascending order  just change to < sign for descending order
for i in range(len(vals)):
    for j in range(i+1,len(vals)):
        if(vals[i]>vals[j]):
            temp=vals[i]
            vals[i]=vals[j]
            vals[j]=temp

print(vals)
