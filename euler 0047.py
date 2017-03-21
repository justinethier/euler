import eulerlib

# The key optimization here is to only use the first
# few primes as possible prime factors
primes = []
for p in eulerlib.PrimesPlus():
    primes.append(p)
    if p > 4000: # Only use first few primes
        break
    
def lGetPrimeDecomp(n):
  ''' Custom version of function from library, to use primes from above '''
  d = {}
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
    
# Search!
npf = 0
for n in range(10 ** 1, 10 ** 6):
    numDiv = lGetPrimeDecomp(n)
    if numDiv != None and len(numDiv) == 4:
        npf += 1
    else:
        npf = 0

    if npf == 4:
        print(n)
        break
