print("Program Started!\n")
letter = input("Please enter a standard character?\n")
if len(letter) == 1:
  print("The ASCII code for {} is {}".format(letter, ord(letter)))
else:
  print("Incorrect character entered!")

print("Program Ended!")

