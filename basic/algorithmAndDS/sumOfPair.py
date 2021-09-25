arr = [1, 5, 7, -1, 5]
n= len(arr)
count = 0
sum = 6
# Consider all possible pairs
# and check their sums and print sum with same pair
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == sum:
            print(arr[i], arr[j])
            count += 1
print(count)