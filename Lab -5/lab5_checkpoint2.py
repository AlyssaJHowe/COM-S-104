def findUserName(name):
    name = name.strip()
    name = name.lower()
    name = name.split()
    firstn = name[1]
    first = firstn[0]
    lastn = name[0]
    last = lastn[ :-1]
    return first + last



name = raw_input("Please enter your name (last name, first name): ")
print findUserName(name)
