first = "nick"
second = "cage"
parent = "actor"
city = "chicago"
phone = "8634871690"
strfind = "o"    # it might be
start = "863"
string1 = "the world is a better place"

first = first.strip()
second = second.strip()
parent = parent.strip()
city = city.strip()
first = first.capitalize()
second = second.capitalize()
parent = parent.capitalize()
print(first + ' ' + second + ' ' + parent + ' ' + city)
print(phone.isdecimal())

print(len(start))
if len(start) == 1:
    print(phone[0] == start)
else:
    flag = 0
    for i in range(0, len(start)):
        if phone[i] == start[i]:
            flag += 1
    print(flag == len(start))

print(len(start))
print(phone[len(start)-1])
print(start==phone[len(start)])
print(phone[0] == start)
fullstring = first + second + parent + city
print(fullstring.count(strfind))
print(string1.split())
print(city.lower().find(strfind.lower()))  # lower case upper case might be the issue