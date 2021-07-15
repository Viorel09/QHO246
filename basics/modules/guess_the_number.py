#using import and use of a module
from random import randrange as r

min = int(input("Please enter the minimum value:"))
max = int(input("Please enter the maximum value:"))

x = int(r(min,max+1))

n = int(input("I'm thinking of a number between {} and {}. Can you guess what it is?\n".format(min,max)))
while n != x:
  if n < x:
    print("Your guess is too low!\nTry again:\n")
    n = int(input())
  elif n > x:
    print("Your guess is too high.\nTry again:\n")
    n = int(input())
else:
  print("Congratulations! Your number is correct!")
