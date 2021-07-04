print("Where should i look?")

place = input().lower()

if place == "in the bedroom":
  print("Where in the bedroom should i look?")
  place2 = input().lower()
  if place2 == "under the bed":
    print("Found some shoes but no battery.")
  else:
    print("Found some mess but no battery.")

elif place == "in the bathroom":
  print("Where in the bathroom should i look?")
  place3 = input().lower()
  if place3 == "in the bathtub":
    print("Found a rubber duck but no battery.")
  else:
    print("Found a wet surface but no battery.")

elif place == "in the lab":
  print("Where in the lab should i look?")
  place4 = input().lower()
  if place4 == "on the table":
      print("Yes! I found my battery!")
  else:
      print("Found some tools but no battery.")

else: 
  print("I do not know where that is but i will keep looking.")
