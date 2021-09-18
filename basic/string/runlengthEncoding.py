#st = "wwwwaaadexxxxxxywww"



st = "aaabab"
n = len(st)
i = 0
while i < n - 1:
    # Count occurrences of
    # current character
    count = 1
    while (i < n-1 and st[i] == st[i+1]):
        count += 1
        i += 1
    i += 1  #to increment the main while loop
    # Print character and its count
    print(st[i - 1] + str(count), end="")
