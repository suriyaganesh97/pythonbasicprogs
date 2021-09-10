def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def calculator(n1, n2, func):
    return func(n1, n2)

result_1 = calculator(5, 3, add)
print(result_1)

result_2 = calculator(5, 3, subtract)
print(result_2)