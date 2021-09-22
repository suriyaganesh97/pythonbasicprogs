n= 5
arr = [1,4,5,6,6]
arr.sort() #after sorting if we oonly display last from second is two people have same first score it wont work
#to overcomne this we are creating a new list without duplicates
arr2 = []
[arr2.append(i) for i in arr if i not in arr2] #list comprehesnion to remove duplicates

print(arr2[len(arr2)-2])