#This script displays the number of boxes necessary to ship a certain amount of an item for Colfax Industries.
from math import ceil
item = input("Enter the quantity of the item: ")
holds = input("How much of the item can a box hold? ")
print "Colfax Industries Shipping Boxes Calculator"
print "Items quantity: " + str(item)
print "Quantity per box: " + str(holds)
box = float(item)/holds
required = ceil(box)
print "Required number of boxes: " + str(required)
if item % holds != 0:
    print "Partially filled box: Yes"
else:
    print "Partially filled box: No"
