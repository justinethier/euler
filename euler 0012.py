import math
from functools import reduce

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
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)
# end stack overflow

f, n = 0, 1
while f < 500:
    n = n + 1
    trinum = n * (n + 1) / 2 # the Nth triangle number

    f = NumberOfDivisors(trinum)
    if (f > 200):
        print(n, trinum, f)
