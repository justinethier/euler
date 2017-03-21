import eulerlib

primes = []
for p in eulerlib.PrimesPlus():
    primes.append(p)
    if p > 4000: # Only use first few primes
        break

def check(n):
    ''' Check to see if a comp num satisfies CG's properties '''
    for p in primes:
        for i in range(1, int(n)):
            if p + (2 * (i ** 2)) == n:
                return (p, i)
    return None

for i in range(9, 10**5 + 1, 2):
    if not eulerlib.isprime(i) and check(i) == None:
        print(i)
        break
