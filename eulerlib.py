'''
The purpose of this module is to collect functions that
are useful for solving project euler problems. For example,
many of the euler problems invole primes, hence many prime
functions are collected here.

Code aggregated and/or written by Justin Ethier
'''
#import itertools
import math
from functools import reduce

def primes(n): 
    '''
    Find all primes less than n
    Example of usage:
        nums = primes(2000000)
	sum = 0
	for x in nums:
	    sum = sum + x	
    '''
    if n==2: return [2]
    elif n<2: return []
    s=list(range(3,n+1,2))
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            #print(int(j))
            if int(j) < len(s): s[int(j)]=0
            while j<half:
                #print(int(j))
                if int(j) < len(s): s[int(j)]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

# from stack overflow:
#Once you have the prime factorization, figuring out how many factors there are is straightforward. Suppose the prime factors are p1, p2, ..., pk and they are repeated m1, m2, ..., mk times. Then there are (1+m1)(1+m2)...(1+mk) factors
import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  '''
  Find the number of divisors of the given number
  '''
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)
# end stack overflow

def GetPrimeFactors(n):
  d = []
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d.append(p) #d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def is_pandigital(n):
        ''' Determine if integer n is pandigital'''
        l = list(str(n))
        l.sort()
        for i in range(0, len(l)):
                if l[i] != str(i+1):
                        return False
        return True


def nCr(n, r):
    ''' nCr (n choose r) probability function '''
    return fac[n] / (fac[r] * fac[n - r])

