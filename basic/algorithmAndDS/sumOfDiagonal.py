A = [[7,1,5],[1,2,3],[4,0,6]]
M = 3
sum = 0
for i in range(0, M):
   for j in range(0, M):
      if i == j:    #capturing 0,0 1,1, and 2,2 elements
         sum = sum + A[i][j]
      elif i + j == M-1:     #capturing 0,3 and 2,0 elements of matrix here if we dont sue elif the number at 1,1 will get added again to the sum
         sum = sum + A[i][j]
print(sum)
