'''
Solution to project euler #27

Find a quadratic formula that produces the maximum number of primes for consecutive values of n.
http://projecteuler.net/index.php?section=problems&id=27

Justin Ethier, 2010
'''
import eulerlib

def nP4Quad(a, b):
    '''
    Calculate number of primes for n**2 + an + b
    Where a, b are integers and n starts from 0
    '''
    n = 0 # Num of primes
    while True:
        if not eulerlib.isprime( n**2 + (a * n) + b ):
            break
        n += 1
    return n

ma, mb, mprimes = 0,0,0
factor = 100

# b must be prime becuase otherwise test fails when n == 0
brange = eulerlib.primes(1000)
nbrange = []
for prime in brange:
    nbrange.append(prime * -1) 
brange += nbrange # Add neg version of the primes
###

# Search the problem space...
for a in range(-9 * factor, 10 * factor):
    for b in brange:
        if eulerlib.isprime(a + b + 1): # Cull at n == 1 (probably not needed)
            nprimes = nP4Quad(a, b)
            if nprimes > mprimes:
                ma, mb, mprimes = a, b, nprimes

print("Solution: a = %d, b = %d, nprimes = %d, a*b = %d" % (ma, mb, mprimes, ma * mb))
