#---------------------------#
# Michael Beaver            #
# 6 June 2015               #
#---------------------------#
# Project Euler 12          #
#                           #
# Find the first triangle   #
# number to have over 500   #
# divisors.                 #
#---------------------------#

import math

n = 8
found = False
t = 0

while (found == False):
    count = 2
    t = int((n * (n + 1)) / 2)
    bound = math.floor(math.sqrt(t))
    idx = 2

    while (idx < bound):
        if (t % idx == 0):
            count = count + 2
        idx = idx + 1

    if (count > 500):
        found = True
    else:
        n = n + 1

print(t)

        
