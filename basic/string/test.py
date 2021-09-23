alpha = ""
for i in range(ord('A'),ord('Z')+1):
    a = chr(i)
    alpha += a

def num_conv(num):
    q = num//26
    r = num%26
    if num < 26:
        return alpha[num-1]
    else:
        if r==0:
            if q == 1:
                return alpha[r-1]
            else:
                return num_conv(q-1) + alpha[r-1]
        else:
            return num_conv(q) + alpha[r-1]

print(num_conv(26))
print(num_conv(51))
print(num_conv(52))
print(num_conv(80))
print(num_conv(676))
print(num_conv(702))
print(num_conv(705))