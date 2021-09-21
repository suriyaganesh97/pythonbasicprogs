a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
k = 0
l = 0
m = 4  #this you can set by len(a[0])
n = 4


''' k - starting row index
    l - starting column index 
    m - ending row index
    n - ending column index
    i - iterator '''
#range will run only till value sepcified - 1
# but in print we should specify the end value as well
while (k < m and l < n):
    # Print the first row from
    # the remaining rows
    for i in range(l, n):
        print(a[k][i], end=" ")

    k += 1

    # Print the last column from
    # the remaining columns

    for i in range(k, m):
        print(a[i][n - 1], end=" ")

    n -= 1

    # Print the last row from
    # the remaining rows
    # Print the bottom row, i.e. if k < m,
    # then print the elements of m-1th row from column n-1 to l and decrease the count of m
    if (k < m):

        for i in range(n - 1, (l - 1), -1):
            print(a[m - 1][i], end=" ")

        m -= 1

    # Print the first column from
    # the remaining columns
    if (l < n):
        for i in range(m - 1, k - 1, -1):
            print(a[i][l], end=" ")

        l += 1
