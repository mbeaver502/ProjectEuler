#---------------------------#
# Michael Beaver            #
# 4 June 2015               #
#---------------------------#
# Project Euler 6           #
#                           #
# Find the difference       #
# between the sum of the    #
# squares of the first 100  #
# natural numbers and the   #
# square of the sum.        #
#                           #
# Use simple summation rules#
# to derive:                #
#    [n(3n+2)(n^2-1)]/12    #
#---------------------------#

bound = 100

sol = bound
sol = sol * (3 * bound + 2)
sol = sol * (bound * bound - 1)
sol = sol / 12

print("Solution: ", sol)
