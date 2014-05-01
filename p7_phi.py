#!/usr/bin/env python
"""
Practical 7

Implement the following routine: 
	
	Integer phi(Integer)

such that phi(n) will return phi(n)
http://deadendmath.com/euler-phi-function/
"""

import p1_gcd

def phi(n):

    phi = 0
    i = 1
    while i < n:
        the_gcd = p1_gcd.gcd(n,i)
        if the_gcd == 1:
            phi += 1
        i = i + 1
    return phi

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 7 - Phi"
	#over 300 digit long integers
	longint1 = 355555**62
	longint2 = 429024**70

	print phi(20)
	print phi(1) #= 1
	print phi(2) #= 1
	print phi(20) #= 8
	print phi(36) #= 12
	print phi(81) #= 54
	print phi(90) #= 24
	print phi(100) #= 40
	print phi(9007199254740881) #= 9007199254740880
	print phi(9007199254740997) #= 9007199254740996
	print phi(999999999999999999) #= 441994921381739520
	print phi(9999999999999999999) #= 6666666666666666660
	print phi(99999999999999999999) #= 58301444908800000000
	
	print "Done."