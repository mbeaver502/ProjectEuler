#---------------------------#
# Michael Beaver            #
# 5 June 2015               #
#---------------------------#
# Project Euler 10          #
#                           #
# Find the sum of all the   #
# primes below 2,000,000.   #
#---------------------------#

# https://primes.utm.edu
file = open("primes.txt")

total = 0
line = file.readline()
while (line != "eof"):
    if (line != '\n'):
        total = total + int(line, 10)
    line = file.readline()

file.close()

print("Sum:", total)

        
