#---------------------------#
# Michael Beaver            #
# 2 June 2015               #
#---------------------------#
# Project Euler 1           #
#                           #
# Find the sum of all the   #
# multiples of 3 or 5 below #
# 1000.                     #
#---------------------------#

idx = 0
multSum = 0

while (idx < 1000):
    if (idx % 3 == 0 or idx % 5 == 0):
        multSum = multSum + idx
    idx = idx + 1

print("Sum: ", multSum)


