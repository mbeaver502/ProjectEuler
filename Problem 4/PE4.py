#---------------------------#
# Michael Beaver            #
# 3 June 2015               #
#---------------------------#
# Project Euler 4           #
#                           #
# Find the largest palin-   #
# drome made from the       #
# product of two 3-digit    #
# numbers.                  #
#---------------------------#

def isPalindrome(x):
    """Determines if x is a palindrome."""
    num = str(x)
    size = len(num)
    i = 0
    j = size - 1

    while (i < j):
        if (num[i] != num[j]):
            return False
        i = i + 1
        j = j - 1

    return True


#------------------------------------------------------

bound = 999
palindromes = list()
i = bound


print("Working", end='')

while (i >= 100):
    print(".", end='')
    j = bound
    
    while (j >= 100):
        product = i * j
        if (isPalindrome(product)):
            palindromes.append(product)
        j = j - 1
            
    i = i - 1

print("\nFound ", len(palindromes), " palindromes")
print("Largest: ", max(palindromes))


        
