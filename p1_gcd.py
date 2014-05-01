#!/usr/bin/env python
"""
Practical 1

Use Euclid's algorithm to implement the routine:

	Integer gcd(Integer; Integer)
"""

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    #print a, b
    while b > 0:
        a, b = b, a%b
        #print "working ... " ,a , b

    return a

#####################################################################
# Tests
	
if __name__ == "__main__":
	
	import fractions

	#over 300 digit long integers
	longint1 = 355555**62
	longint2 = 352345**70

	print "Practical 1"
	print "Calculate the Greatest Common Divisor of a and b"
	print gcd(23, 67)
	print gcd(67, 23)
	print gcd(48, 180)
	print gcd(48, 18)

	print gcd(longint1, longint2)
	print fractions.gcd(longint1, longint2)

	print "Done."