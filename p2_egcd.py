#!/usr/bin/env python	
"""

The Extended Euclidean Algorithm
We can use the Extended Euclidean Algorithm to solve the equation ax + by = gcd(a; b) for x and y.

Use the Extended Euclidean Algorithm to implement the routine:

	(Integer; Integer; Integer) gcde(Integer; Integer)

where a call gcde(a; b) of this routine should return a tuple (g; x; y) of three integers such that:
- g = gcd(a; b)
- a  x + b  y = g
"""

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

#####################################################################
# Tests
	
if __name__ == "__main__":
	
	import fractions

	#344 character long
	longint1 = 352345**62
	longint2 = 352345**70

	print "Practical 2"
	print egcd(42, 56)
	print egcd(23, 67)
	print egcd(48, 180)
	print egcd(48, 18)
	print "Done."