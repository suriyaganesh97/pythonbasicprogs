fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]    #nested list
print(fruits)
print(fruits[1])   #grapes is printed and not apples
fruits[2] = "guava"
print(fruits)
fruits.append("pomegranate")
print(fruits)
print(dirty_dozen)
print(dirty_dozen[0])   #this refers to first element which is list fruit in the list dirty dozen
print(dirty_dozen[1])
print(dirty_dozen[1][2])