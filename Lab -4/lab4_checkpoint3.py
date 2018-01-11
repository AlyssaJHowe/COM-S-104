from sample_functions import sing_verse, simple_postage

#99Bottles
num = input("Enter a number between 1 and 99: ")
sing_verse(num)

#Postage
weight = input("Enter the weight of your letter in ounces (up to 3.5): ")
simple_postage(weight)
cost = simple_postage(weight)
print "The postage cost to send this letter is $" + str(cost)
