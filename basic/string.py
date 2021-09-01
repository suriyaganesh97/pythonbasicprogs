str1 = "suriya"
str2 = "ganesh"

print(str1+str2)
print(str1+" "+str2)
print(str1*3)
print(str1+"\n"+str2)
print(str1+"\t"+str2)
print(str1[0])
print(str1.find('u'))  # in place of a char or string u can also pass a string variable
print(str1.replace('ri','r'))
print(str1.count('s'))
print(str1.capitalize())
print(r"\nsuriya\tganesh")  #raw string

str3 = " suriya ganesh"
print(str3.strip())  #strip is used for removing spaces only at beginning and end
print(str3.replace(" ",""))  #replaces blank spaces with no space in a string
print(str3)

str4 = "753888682a"
print(str4[0] == '6')
print(str4.isdecimal())