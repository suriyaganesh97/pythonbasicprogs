# a=1 z= 26   az = 52
list_1 = []
for i in range(ord('a'), ord('z')+1):
    a = chr(i)
    list_1.append(a)
user_char = input("input a char to find its row: ")

final_string = ""
for i in user_char:
    pos = list_1.index(i)
    final_string += str(pos+1)
print(final_string)