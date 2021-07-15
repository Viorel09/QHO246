#while loop performing user input calculations
print("How many numbers should I sum up?")
n = int(input())
sum = 0
total = 0

while (sum < n):
  print("Please enter number", sum, "of", n, ":")
  n1 = int(input())
  total = total + n1
  sum = sum + 1

print("The answer is", total)
