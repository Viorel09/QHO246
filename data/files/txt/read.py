#reading of text file

def search(locations):
  print("Searching...\n")
  with open("data/files/txt/locations.txt") as file:
    data = file.readlines()
    for line in data:
      print("Looked in", line.strip())
  print("\n...Done!")

def run():
  search("data/files/txt/locations.txt")

run()