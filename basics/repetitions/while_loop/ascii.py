print(" How many bars should be charged?")
response = int(input())
bars = 0
d = "\u275A"
while bars < response:
  bars += 1
  print("Charging:" , d*bars)


print("The battery is fully charged.")
