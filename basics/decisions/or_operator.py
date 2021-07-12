print("What type of adventure should i have?")

kind = input().lower()

if ((kind == "scary") or (kind == "short")):
  print("Entering the dark forest!")

if ((kind == "safe") or (kind == "long")):
    print("Taking the safe route!")
else:
  print("Not sure which route to take")
