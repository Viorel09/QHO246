# Calculating body mass
print("What is your name human?")
name = input()
#when you use input() function the default data type is a string!
print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weight (in kilograms)?")
weight = float(input())

bmi = weight / (height**2)

#print(f"{name} you are {age} old and your BMI is {bmi}")
#concatenation of strings (join them togheter)
#print(name +" you are " + str(age) + " years old and your bmi is " + str(bmi))
print("{} you are {} years old and your bmi is {:.2f}".format(name, age, bmi))
