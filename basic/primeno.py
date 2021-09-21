a = int(input("enter a number: "))
if a > 1:
    # Iterating over the given number with for loop
    for j in range(2, int(a / 2) + 1):
        # If the given number is divisible or not
        if (a % j) == 0:
            print(a, "is not a prime number")
            break
            # Else it is a prime number
    else:
        print(a, "is a prime number")
    # If the given number is 1
else:
    print(a, "is not a prime number")