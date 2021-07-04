print("Towards which direction should I paint (up, down, left or right)?\n")

d = input().lower()

if d == "up":
  print("\nI am painting in the upward direction!\n")

elif d == "down":
  print("\nI am painting in the downwards direction!\n")

elif d == "left":
  print("\nI am painting towards the left hand side!\n")

elif d == "right":
  print("\nI am printing towards the right hand side!\n")

else:
  print("\nAs you have not chose any suitable direction for me i will start painting in circles!\n")