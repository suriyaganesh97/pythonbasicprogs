weight = float(input("enter your weight in kg "))
height = float(input("enter your height in M "))
bmi = int(weight / height ** 2)  #this means height to the power of 2
print("your BMI is "+str(bmi))
if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal")
elif bmi < 30:
    print("you are overweight")
else:
    print("you are obese")
