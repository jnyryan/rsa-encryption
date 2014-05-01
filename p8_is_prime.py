#!/usr/bin/env python
"""

Implement the following routine:
	
	Boolean fermat(Integer, Integer)

such that fermat(x,t) will use Fermat's algorithm to determine if x is prime.

REMEMBER
Fermat's theorm asserts that if n is prime and 1<=a<=n, then a**n-1 is congruent to 1(mod n)


"""

import p5_expm
import random

def is_prime(n, t):

    for i in xrange(1, t):
    	a = random.randint(2, n-1)
    	#r = (a**n-1) % n
    	r = p5_expm.expm(a, n-1, n)
    	#print a , r
    	if r != 1:
    		return False

    return True

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 8 - Verify a number is prime using Fermats Theorem"
	t = 30
	print is_prime(3, t)	
	print is_prime(4, t)	
	print is_prime(5, t)	
	print is_prime(6, t)	
	print is_prime(7, t)	
	print is_prime(11, t)	
	print is_prime(13, t)	
	
	print is_prime(101, t)	
	print is_prime(294000, t)
	print is_prime(294001, t)	
	print "Done."