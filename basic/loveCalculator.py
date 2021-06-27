name1 = input("what is your name ")
name2 = input("what is her name ")
name1 = name1.lower()
name2 = name2.lower()
count_true_1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
count_true_2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
count_love_1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
count_love_2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
score = int((str(count_true_1 + count_true_2) + str(count_love_1 + count_love_2)))
if score < 10 or score > 90:
    print(f"your score is {score} ,  you go together like coke and mentos ")
elif  score < 50 and score > 40:
    print(f"your score is {score} , you are alright together ")
else:
    print(f"your score is {score}")

