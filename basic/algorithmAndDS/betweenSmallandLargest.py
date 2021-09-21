arr1 = [1,2,5,10]
high_no = max(arr1)
small_no = min(arr1)
# if needed na sort and then get highest and lowest from sorted values
for i in range(small_no,high_no + 1):
    if i not in arr1:
        print(i,end=" ")