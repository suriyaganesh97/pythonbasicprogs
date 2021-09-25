#st = "wwwwaaadexxxxxxywww"

st = "aaabba"
n = len(st)
i = 0
while i < n:
    # Count occurrences of
    # current character
    count = 1   #initialise count to 1 since the letter is present at least once
    while (i < n-1 and st[i] == st[i+1]):
        count += 1
        i += 1
    i += 1  #to increment the main while loop
    # Print character and its count
    print(st[i - 1] + str(count), end="")
