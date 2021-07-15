#using count with whileloop
print("How many live cables must I avoid?")
n = int(input())
x = 0

while x < n:
  print("Avoiding...", end ="")
  x += 1
  print("...Done! {} live cable avoided!".format(x))

print("All live cables have been avoided")
