#This script has a function written out that will determine if an integer
#is equal to the sum of its own digits each raised to the power of the number of digits (a plus perfect number).
def is_plus_perfect(integer):
    digitsInt = len(str(integer))
    digitPowerSum = 0
    for i in str(integer):
        digitPowerSum = digitPowerSum + int(i)**digitsInt 
    if digitPowerSum == integer:
        return "a plus perfect number"
    else:
        return "not a plus perfect number"

#User input that gets inserted into the above function
num = input("Enter a positive number: ")
if num < 0:
    print "Error: Not a positive number"
else:
    print "Number", num, "is", is_plus_perfect(num)
