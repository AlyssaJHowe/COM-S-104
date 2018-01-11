#This script contains two functions that calculate order totals for customers of ManyHats.com

#This function calculates order totals at the prices of $10 per hat, $50 for a box of six hats, and $2 shipping per hat.
def order_total(num):
    hatsOrdered = num
    if hatsOrdered < 6:
        totalCost = 10 + 2*hatsOrdered
    else:
        totalCost = (hatsOrdered / 6)*50 + (hatsOrdered % 6)*10 + 2*hatsOrdered
    return totalCost
#Lacks a print statement so that part(C) works properly and one wasn't mentioned in the instructions.

#Due to demand, Manyhats started offering overnight shipping with new shipping costs.
#This function calculates order totals at the prices of $10/hat and varying shipping prices:
#$32 for 5 or fewer hats, $45 for more than 5 but less than 21 hats, or $3/hat for more than 20 hats.
def order_total_overnight(num):
    addedCosts = (10*num)
    hatsOrdered = num
    if hatsOrdered <= 5:
        totalCost = (addedCosts + 32)
    if hatsOrdered > 5 and hatsOrdered <= 20:
        totalCost = addedCosts + 45
    if num > 20:
        totalCost = addedCosts + ((3*addedCosts)/10)
    return totalCost
#Lacks a print statement so that part(C) works properly and one wasn't mentioned in the instructions.




        
        
