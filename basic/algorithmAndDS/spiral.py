a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

# print(a[0][0])

for i in range(0, len(a) - 1):
    for j in range(0, i):
        print(a[i][j])
