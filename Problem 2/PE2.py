#---------------------------#
# Michael Beaver            #
# 2 June 2015               #
#---------------------------#
# Project Euler 2           #
#                           #
# Find the sum of the even- #
# valued terms in the       #
# Fibonacci Sequence. Do not#
# exceed 4,000,000.         #
#---------------------------#

limit = 4000000
idx1 = 1
idx2 = 2
fibSum = 0

while (idx2 < limit):
    if (idx2 % 2 == 0):
        fibSum = fibSum + idx2
    temp = idx2
    idx2 = idx1 + idx2
    idx1 = temp
    
print("Sum: ", fibSum)
