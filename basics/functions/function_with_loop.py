def cross_bridge(step):
  a = 0
  while a < step:
    print("Crossed Step")
    a += 1
  if a <= 5:
    print("We must keep going!")
  else:
    print("The bridge is collapsing!")

cross_bridge(3)
cross_bridge(6)
