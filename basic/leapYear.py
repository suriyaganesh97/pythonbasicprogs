
year = int(input("enter a year to to check leap year or not "))
if year % 4 == 0:
    if year % 400 == 0:
        print("leap year ")
    elif year % 100 == 0:
        print("not a leap year ")
    else:
        print("leap year")
else:
    print("not a leap year ")
