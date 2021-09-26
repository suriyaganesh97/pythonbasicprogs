str1 = "abcde"
str2 = "deabc"

if len(str1) != len(str2):
    print("not a rotating string")
else:
    str1 = str1 + str1
    if str1.index(str2):
        print("Second string is a rotation of first string");
    else:
        print("Second string is not a rotation of first string");