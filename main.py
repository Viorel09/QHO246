
def search(locations):
  print("Searching...")
  with open("data/files/txt/locations.txt") as file:
    data = file.readlines()
    for line in data:
      print("Looked in", line.strip())
  print("\n...Done!")
search(1)