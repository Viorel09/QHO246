while True:
  print("Please choose an option\n\n1-Nice message\n2-Area of a rectangle\n3-Area of a triangle\n4-Multiplication table\n0-Exit the application")

  option = int(input())

  if option == 1:
    print("You don't smell so bad today!")

  #long way of writing
  # elif option == 2:
  #   print("Enter the leght of the rectangle")
  #   l = float(input())
    
  #another way to write
  elif option == 2:
    l = float(input("Enter the lenght of the rectangle: "))
    w = float(input("Enter the height of the rectangle: "))
    print("Area of this rectangle is {:.2f}" .format(l*w))
    
  elif option == 3:
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    print("Area of this triangle is {:.2f}".format(b*h/2))

  elif option == 4:
    n = int(input("Enter the number: "))
    counter = 0
  # print(f"{n}x1 = {n*1}")
  # print(f"{n}x2 = {n*2}")
  # print(f"{n}x3 = {n*3}")
    n2 = int(input("Enter the limit of the table: "))

  # print(f"{n}x10 = {n*10}")

    while counter <= n2:
      print(f"{n}x{counter} = {counter*n}")
      counter += 1
  #was previously counter = counter + 1

    print("End of calculations")

  elif option == 0:
    print("Closing application, bye!")
    break

  else:
    print("Go to Specsavers, to check the eyes!")