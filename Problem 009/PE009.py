#---------------------------#
# Michael Beaver            #
# 4 June 2015               #
#---------------------------#
# Project Euler 9           #
#                           #
# Find the product abc for  #
# the Pythagorean triplet   #
# such that a + b + c is    #
# equal to 1000.            #
#---------------------------#

def pythagoreanTriplet(n):
    """ Finds the Pythagorean triplet for n. """
    
    triplet = tuple()
    for a in range(1, n, 1):
        for b in range(1, n - a, 1):
            c = n - a - b
            if (a * a) + (b * b) == (c * c):
                triplet = triplet + (a, b, c)
                return triplet
            
    return None

#------------------------------------------------------

solution = pythagoreanTriplet(1000)

if (solution != None):
    a = solution[0]
    b = solution[1]
    c = solution[2]

    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("abc: ", a * b * c)

else:
    print("No solution found.")
