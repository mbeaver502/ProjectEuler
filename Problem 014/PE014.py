#---------------------------#
# Michael Beaver            #
# 11 June 2015              #
#---------------------------#
# Project Euler 14          #
#                           #
# Find the starting number  #
# under 1,000,000 producing #
# the longest chain in the  #
# Collatz Sequence.         #
#---------------------------#

n = 1
bound = 1000000
largest = (0, 0)

while (n < bound):
    count = 0
    _n = n
    
    while (_n != 1):
        if (_n % 2 == 0):
            _n = int(_n / 2)
        else:
            _n = (3 * _n) + 1
        count += 1
        
    count += 1
    if (count >= largest[1]):
        largest = (n, count)
    n += 1

print(largest)
