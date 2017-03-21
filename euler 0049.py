# Solution to Project Euler #49
#
# by Justin Ethier
#
import eulerlib
import itertools

# Find all 4 digit primes
primes = []
for p in eulerlib.PrimesPlus():
    if p > 10**3:
        if eulerlib.isprime(p):
            primes.append(p)
        if p > 10**4:
            break

# Collect primes that are permutations of same digits
seqs = {}
for p in primes:
    bucket = list(str(p))
    bucket.sort()
    key = int("".join(bucket))
    if key in seqs:
        # Existing bucket, add p
        seqs[key].append(p)
    else:
        # New bucket, add p
        seqs[key] = [p]

# Find solutions - that is, sequences of primes that increase by 3330    
def check(l):
    ''' Check a single 3-element list to see if it is a solution '''
    l.sort()
    if l[1] - l[0] == l[2] - l[1] and l[2] - l[1] == 3330:
        return True
    return False

def listCheck(lst):
    ''' Check a list for subsets that are solutions '''
    for l in itertools.combinations(lst, 3):
        if check(list(l)):
            print(l)

for key in seqs.keys():
    listCheck(seqs[key])
