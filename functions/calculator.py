

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide
              }

def calculator():
    num1 = float(input("enter the first number: "))
    for symbol in operations:
        print(symbol)
    continue_or_not = True
    while continue_or_not:
        operation_symbol = input("enter the operation which you wish to perform: ")
        num2 = float(input("enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")
        if input(f"type y to work with {answer} or press n to start a new calculation ") == 'y':
            num1 = answer
        else:
            continue_or_not = False
            calculator()


calculator()