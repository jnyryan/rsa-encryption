#!/usr/bin/env python
"""
Practical 5

Using the square-and-multiply algorithm, implement the following routine:
Integer expm(Integer, Integer, Integer)
such that expm(m, a, k) computes a**k modulo m.
"""

def expm( a, k, n):
	r = 1
	bits = list(bin(k)[2:])
	for bit in bits:
		r = (r * r) % n
		if int(bit) == 1:
			r = (r * a) % n
	return r

# http://www.programminglogic.com/fast-exponentiation-algorithms/
# http://eli.thegreenplace.net/2009/03/28/efficient-modular-exponentiation-algorithms/

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 5 - Square and Multiply"
	
	print expm(5,40,7)
	print "builtin result: ", pow(5,40,7)
	print expm(5,41,7)
	print "builtin result: ", pow(5,42,7)
	print expm(57678687678,65889,101)
	print "builtin result: ", pow(57678687678,65889,101)
	

	#print expm(101, longint1, 65537)
	
	print "Done."