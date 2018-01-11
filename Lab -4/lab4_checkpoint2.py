def circle_area(x):
    area = 3.14 * x * x
    return area

x = input("Enter the radius of the cylinder: ")
y = input("Enter the height of the cylinder: ")
volume = y * circle_area(x)
print "The volume of the cylinder is", volume
