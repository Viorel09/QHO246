#Initialise empty dictionary
phonebook = {}
#Initialise non-empty dictionary
piotr_data = {"Name": "Piotr", "Age":88, "Doggo": False}
#Search a dictionary
print(piotr_data["Age"])
#Populate the dictionary
phonebook["Frank"] = 6543213546
phonebook["Loki"] = 3215132546
phonebook["Haga"] = 6543213546
phonebook["Loki"] = 1321351315
print(phonebook)

#Populating dictionary more efficiently
for i in range(5):
  phonebook[input("Enter the name: ")] = input("Enter the number: ")
print(phonebook)
#Accesing by value
for i in piotr_data.values():
  if i:
    print("Dog!")
  else:
    print("No Dog!")

for i in piotr_data.items():
  print(i)
  