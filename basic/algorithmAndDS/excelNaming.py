# a=1 z= 26   az = 52
alpha = ""
for i in range(ord('A'), ord('Z')+1):
    a = chr(i)
    alpha += a
#print(alpha)

def num_hash(num):
    if num < 26:
        return alpha[num - 1]
    else:
        q = num // 26
        r = num % 26
        if r == 0:
            if q == 1:
                return alpha[r-1]     # 26 value is captured here
            else:  #captures value like 52,78 where last code is Z and for rest the function is called recursively
                return num_hash(q - 1) + alpha[r - 1]
        else:   #captures value like 51 where rem is not zero so function called to find first code while last code is printed from alpha
            return num_hash(q) + alpha[r - 1]


# num = int(input("enter a value: "))
# print(num_hash(num))

print(num_hash(26))
print(num_hash(51))
print(num_hash(52))
print(num_hash(80))
print(num_hash(676))
print(num_hash(702))
print(num_hash(705))
