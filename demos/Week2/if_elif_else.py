status = int(input("Enter status: "))

if status == 1:
  print("The status was 1")

print("This always prints!")

age = int(input("What is your age ?"))

if age < 20:
  print("You are a child")

elif age <= 30 and age >= 20:
  print("You are a grown up, deal with it")

elif age > 65:
  print("You are old mate!")

else:
  print("You are an adult")
