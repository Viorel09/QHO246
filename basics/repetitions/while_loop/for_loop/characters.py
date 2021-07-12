print("What strange marking do you see?")
x = input()
print("\nIdentifying...")
for position in range(0, len(x)):
  print("index {} :".format(position) + x[position])

print("\nDone!")
