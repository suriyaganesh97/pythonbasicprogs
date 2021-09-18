# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new_num_list = [num**2 for num in numbers]
# print(new_num_list)
# result = [num for num in numbers if num % 2 == 0]

f = open("file1.txt", "r")
list1 = f.readlines()
list_mod1 = [int(num.strip()) for num in list1]
print(list_mod1)

f = open("file2.txt", "r")
list2 = f.readlines()
list_mod2 = [int(num.strip()) for num in list2]
print(list_mod2)


result = [num for num in list_mod1 if num in list_mod2]
print(result)
