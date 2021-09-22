n= 5
arr = [1,4,5,6,6]
arr = list(arr)
arr.sort()

arr2 = []
[arr2.append(i) for i in arr if i not in arr2]

print(arr2[len(arr2)-2])
# [res.append(x) for x in test_list if x not in res]