'''
Created on Jan 9, 2013

@author: anujacharya
'''
# On CodeEval, test cases are read in from a file which is the first argument to your program
# Open the file and read in line by line. Each line represents a different test case
# (unless given different instructions in the challenge description)
import sys

from math import sqrt

def basicSieve(n):
    """Given a positive integer n, generate the primes < n."""
    s = [1]*n
    for p in xrange(2, 1+int(sqrt(n-1))):
        if s[p]:
            a = p*p
            s[a::p] = [0] * -((a-n)//p)
    for p in xrange(2, n):
        if s[p]:
            yield p 

def primes_sieve(limit):
    limitn = limit+1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes
#def main():
#    for test in test_cases:
#        result = primes(int(test))
#        print result
                
if __name__ == "__main__":
    test_cases = open(sys.argv[1], 'r')
    result = []
    for test in test_cases:
        result = primes_sieve(int(test))
        print ','.join(map(str, result))
    test_cases.close()