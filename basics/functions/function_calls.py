#display name in box
word = input("Insert word:")

def display_box(word):
  message = "* {} *".format(word)
  print("*" * (len(message)))
  print(message)
  print("*" * (len(message)))

def lower_case(word):
  print(word.lower())

def upper_case(word):
  print(word.upper())

def mirrored(word):
  b = ""
  for c in word:
    b = c + b
  print(word, "|" ,b)

def repeat(word):
  n = int(input("How many times do you want to repeat?"))
  for count in range(1,n+1,1):
    upper_case(word),lower_case(word)

def option():
  x = input("Choose an option: 1 - 5\n")
  if x == "1":
    display_box(word)
  elif x == "2":
    lower_case(word)
  elif x == "3":
    upper_case(word)
  elif x == "4":
    mirrored(word)
  elif x == "5":
    repeat(word)
  else:
    print("Bad input")

option()