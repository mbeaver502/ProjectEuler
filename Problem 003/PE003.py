#---------------------------#
# Michael Beaver            #
# 3 June 2015               #
#---------------------------#
# Project Euler 3           #
#                           #
# What is the largest prime #
# factor of the number      #
# 600851475143? (uses trial #
# division, so very slow)   #
#---------------------------#

import math

#----------------------------------------------------------

def getFactors(n):
    """Gets the factors of n using trial division."""
    
    bound = math.ceil(math.sqrt(n))
    factors = list()
    idx = 2
    
    while (idx < bound):
        if (n % idx == 0):
            factors.append(idx)
            factors.append(math.floor(n / idx))
        idx = idx + 1

    return factors

#----------------------------------------------------------

n = 600851475143

factors = getFactors(n)
primes = list()
size = len(factors)
i = 0

while (i < size):
    if (len(getFactors(factors[i])) == 0):
        primes.append(factors[i])
    i = i + 1

print("Original value: ", n)
print(" Largest prime: ", max(primes))


