num = input("How many moustraps? ")
if num <= 50:
    total = num * 2.00
    r = raw_input("Are you an Iowa resident (y/n)?")
    if r == "y":
        print "Subtotal: " + str(total)
        tax = total*.06
        print "Tax: " + str(tax)
        total = total+tax
        print "Total: " + str(total)
    else:
        print "Total: " + str(total) 
else:
    first = 50 * 2.00
    extra = (num - 50) * 1.50
    total = first + extra
    r = raw_input("Are you an Iowa resident (y/n)?")
    if r == "y":
        print "Subtotal: " + str(total)
        tax = total*.06
        print "Tax: " + str(tax)
        total = total+tax
        print "Total: " + str(total)
    else:
        print "Total: " + str(total) 
