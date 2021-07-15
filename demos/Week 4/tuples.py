from math import pi

def students_marks():
  name = input("enter students name: ")
  mark = float(input(f"Enter the mark for {name} : "))
  return name,mark


#x,y = students_marks()
#print(x)
#print(y)
#y = y + 10
#t = x,y
#print(t)

def area_and_circ(radius):
  area = pi*radius**2
  circ = 2*pi*radius
  return area,circ,radius


def run():
  tuplex = area_and_circ(float(input("Enter radius of your circle: ")))
  print(f"The area of your circle is {tuplex[0]:.2f} and circumference is {tuplex[1]:.2f} for a circle of radius {tuplex[2]}")

#print("The area of your circle is {} and circumference is {}".format(tuplex[0], tuplex[1]))

run()