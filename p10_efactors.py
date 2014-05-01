#!/usr/bin/env python
"""
Practical 10

Implement the following routine: 

	Integer* efactors(Integer)

That will determine the prime factors of an integer value n that is the product of two primes. 
This function should use a more efficient algorithm than trial division and should be capable of 
factoring numbers such as 709138557871512933443

http://mathforum.org/library/drmath/view/65801.html

"""

import random

def efactors(n):
	return 3

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 10 - eFactors"
	
	print efactors(10)	
	
	print "Done."