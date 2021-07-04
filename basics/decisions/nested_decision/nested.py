print("What type of cover does the book have (soft or hard)?\n")

cover = input().lower()

if(cover == "soft"):
  print("Is the book perfect bound?")
  perfect_bound = input().lower()

  if (perfect_bound == "yes"):
    print("Soft covers, perfect bound books are very popular!")
  else:
    print("Soft covers with coils and stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")
