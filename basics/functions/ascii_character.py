print("Program Started!\n")
print("Please enter an ASCII code:")
x = abs(int(input()))
if x in range(32,127):
  print("The character represented by the ASCII code {} is {}".format(x, chr(x)))

else:
  print("This is an error. Invalid number code")

print("Program Ended!")