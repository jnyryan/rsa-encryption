#!/usr/bin/env python
"""
Practical 9

Implement the following routine: 

	Integer prime(Integer)

such that prime(d) will use fermats algorithm to produce a d bit prime

"""

import random
import p8_is_prime

def prime(d):
	isprime = False
	while isprime ==  False:
		r = random.getrandbits(d)
		isprime = p8_is_prime.is_prime(r, 30)
	return r

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 9 - Generate a Prime using Fermats Theorem"
	
	print prime(10)	
	print prime(11)	
	print prime(12)	
	print prime(13)	
	print prime(14)	
	print prime(15)	
	print prime(16)	
	print prime(17)	
	print prime(18)	
	print prime(19)	
	print prime(20)	
	print prime(21)	
	print prime(22)	
	
	
	print "Done."