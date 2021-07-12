print("What level of brightness is required?")
b = int(input())
c = "\u002A"

print("\nAdjusting brightness...")
for b in range(2, b+1, 2):
  print(f"\nBeep's brightness level: {b*c}")
  print(f"Bop's brightness level: {b*c}")

print("\nAdjustments complete!")
