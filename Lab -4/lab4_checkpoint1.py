def even_or_odd(s):
    result = len(s)
    print result

    a= result % 2
    if a == 0:
        print "Even"
    else:
        print "Odd"
even_or_odd("Steve")
even_or_odd("Mary")
