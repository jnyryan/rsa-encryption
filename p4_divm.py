#!/usr/bin/env python
"""

Implement the following routine: 

	Integer divm(Integer, Integer, Integer)

such that divm(m, a, b) computes ab**-1 mod m if it exists.
"""

import p3_invm

def divm(m, a, b):
    inv = p3_invm.invm(m, b)
    print inv
    return (a*inv)%m

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 4"

	print divm(119, 43, 67) # inverse of 67(mod119) is 16, 43*16(mod 119) = 43
	print divm(101, 23, 67)
	print "Done."