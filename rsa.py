#!/usr/bin/env python
"""

Implement RSA as the following routines: 

	(Integer, Integer, Integer) rsaKey(Integer)

Integer rsaEnc(Integer, Integer, Integer) Integer rsaDec(Integer, Integer, Integer)
such that:
	rsaKey(s) will generate an RSA key-pair (n,e,d) where n is an s-bit modulus 
	rsaEnc(n, e, m) will return E(n,e)(m)
	rsaDec(n, d, c) will return D(n,d)(c)

"""

import p1_gcd
import p3_invm
import p5_expm
import p9_prime

def rsaKey(s):
	p=p9_prime.prime(s)
	q=p9_prime.prime(s)
	#p=73
	#q=101
	n=p*q
	phi=(p-1)*(q-1)
	e=37
	d=p3_invm.invm(phi,e)
	print p,q,n,phi,e,d
	
	return n,e,d

def rsaEnc(n,e,m):
	
	return p5_expm.expm(m, e, n)

def rsaDec(n,d,c):

	return p5_expm.expm(c, d, n)
	
#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 11 - RSA"
	s = 16
	message = 1002

	print "Message: ", message
	
	n,e,d = rsaKey(s)
	print "keys n,e,d: ",n,e,d
	
	cipher = rsaEnc(n,e,message)
	print "cipher: ",cipher
	
	message = rsaDec(n,d,cipher)
	print "message:",message	
	
	print "Done."