/*
 
 ==================================================================================

 Michael Beaver
 Project Euler 028
 24 Aug 2016
 
 ==================================================================================
 
 Starting with the number 1 and moving to the right in a clockwise direction a 
    5 by 5 spiral is formed as follows:
 
                        21 22 23 24 25
                        20  7  8  9 10
                        19  6  1  2 11
                        18  5  4  3 12
                        17 16 15 14 13
 
 It can be verified that the sum of the numbers on the diagonals is 101.
 
 What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
    formed in the same way?
 
 ==================================================================================
 
*/

import Foundation

let MATRIX_DIM = 1001;

var sum = 0;
var idx = 1;
var delta = 1;
var deltaCount = 0;

if (MATRIX_DIM % 2 == 1) {

    // Essentially we will add every delta-th number to the sum
    // Delta is incremented by 2 (to the next odd number) every 4 cycles (i.e., 4 diagonals)
    // Delta should be odd (1, 3, 5, 7, 9, ...) and should be MATRIX_DIM - 2 at the end
    while delta < MATRIX_DIM {
        
        sum += idx;
        idx += delta + 1;
        
        deltaCount += 1;
        
        if deltaCount == 4 {
            delta += 2;
            deltaCount = 0;
        }
        
    }
    
    // Final diagonal -- the loop is off by one!
    sum += idx;
    
}

print(sum);