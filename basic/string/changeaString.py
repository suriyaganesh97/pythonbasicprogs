string = "abracadabra"
position = 5
character = "k"
list1 = list(string)
list1[position] = character
string2 = ""
for i in list1:
    string2 += i
print(string2)