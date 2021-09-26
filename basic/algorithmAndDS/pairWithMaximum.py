arr1 = [1,9,10,5,3, -20, -19]
arr1.sort()
n = len(arr1)
prodofLowestno = arr1[0] * arr1[1]
prodofHighestno = arr1[n-1] * arr1[n-2]
if prodofHighestno > prodofLowestno:
    print(arr1[n-1],arr1[n-2],prodofHighestno)
else:
    print(arr1[0],arr1[1],prodofLowestno)