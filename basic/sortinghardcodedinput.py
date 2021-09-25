arr1 = [12,45,32,16,59,78,26]
temp = 0
for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[i] < arr1[j]:  #to sort in ascending just change the sign
            temp = arr1[j]
            arr1[j] = arr1[i]
            arr1[i] = temp
for _ in arr1:
    print(_,end=" ")