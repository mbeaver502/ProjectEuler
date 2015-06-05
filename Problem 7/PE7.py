#---------------------------#
# Michael Beaver            #
# 5 June 2015               #
#---------------------------#
# Project Euler 7           #
#                           #
# Find the 10,001st prime.  #
#---------------------------#

import math

"""
    The 10,000th prime is 104,729. (https://primes.utm.edu/lists/small/10000.txt)
    Primes are odd (except 2), and we can show 104731 is not odd,
        so we use it as our seed.
"""
num = 104731
found = False
count = 0

while (found == False):
    bound = math.ceil(math.sqrt(num))
    count = 0
    
    for i in range (2, bound + 1, 1):
        if (num % i == 0):
            break
        else:
            count = count + 1
            
    if (count == bound - 1):
        found = True
        
    if (found == False):
        num = num + 2  # Primes are odd (except 2)


print("Solution:", num)


        
