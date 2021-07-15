#Declare an empty list
red = []

#Declare a non-empty list
amber = ["Poland", "Portugal", "Romania", "Fiji", "Amber"]

#Printing full list
print(amber)

#Print a single element
print(amber[3])

#Add element to the end of a list
red.append("Brazil")
red.append("Somalia")
red.append("Malta")

#for i in range(3):
  #red.append(input("Enter new red list country: "))


#Insert data onto a list not at the print
red.insert(1,"Ghana")
print(red)
red.insert(3, "Switzerland")
print(red)

#Remove an item the list by name
#red.remove(input("Which country to delete: "))

#Remove an itemfor list by index
red.pop(0)
print(red)

#new_amber_country = red.pop(1)
#amber.append(new_amber_country)
#print(amber)
#print(red)

#Delete an item
del red[1]
print(red)

#Slicing
print("---Slicing---")
print(amber[::2])
#Slicing allows you to pecify start point(included), end point(excluded) and steps.

#reverse from Miroslav
a = "Python is lovely"
print(a[::-1])

#Strings in Python ARE lists!!!!!(kind of)
