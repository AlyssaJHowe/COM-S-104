name = raw_input("What is your name?")
nights = input("How many nights are you staying?")
roomservice= input("What was your room service charge?")
telephone = input("What was your telephone charge?")
totalroom =55*nights
tax = totalroom*0.1
totalbill = telephone + roomservice + totalroom + tax

print "Customer's full name: " , name
print "Number of nights: " , nights
print "Total room service charge($): " , roomservice
print "Total telephone charge($): ", telephone
print "River Bend Hotel Bill (Customer :" , name+")"
print "Total room charge($): ", totalroom
print "Entertainment tax($): " , tax
print "Total bill($): " , totalbill
