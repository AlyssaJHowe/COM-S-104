#Hats.py contains the actual calculation functions. This script takes input from the customer and calls the other file to calculate costs based on the customer's answers.

from hats import  *

num = input("How many hats? ")
overnight_shipping = raw_input("Use overnight shipping (y/n)? ")
#In case the user types "Yes," "Y", etc, these next statements allow Python to properly interpret the customer's answer.
overnight_shipping = overnight_shipping.lower().strip()
overnight_shipping = overnight_shipping[0]

if overnight_shipping == "y":
    print "Your order total is $" + (str(float(order_total_overnight(num))))
else:
    print "Your order total is $" + str(float(order_total(num)))
