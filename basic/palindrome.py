input_string = input("enter a string to check whether palindrome or not: ").lower()
reverse_string = input_string[::-1]
# [::-1] is slice notation list[<start>:<stop>:<step>]
if input_string == reverse_string:
    print(f"the {input_string} is a palindrome")
else:
    print(f"the {input_string} is not a palindrome")