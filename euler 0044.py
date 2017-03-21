# Solution to Project Euler #44
#
# By Justin Ethier
#
def pent(n):
    ''' Calculate pentagonal number at n '''
    return int((n * ((3 * n) - 1)) / 2)

def find(pents, pv):
    ''' Find a solution to euler 44 in given range '''
    for x in range(1, nmax):
        for y in range(x-1, 0, -1):
            if (pents[x] + pents[y]) in pv and \
               (pents[x] - pents[y]) in pv:

                return(pents[x] - pents[y])

# Range of pentagonals to search
nmax = 10**5

# List of pentagonals
pents = list(map(lambda p: pent(p), range(nmax)))

# Lookup table, to quickly find an number is pentagonal
pv = {}
for p in pents:
    pv[p] = p

print( find(pents, pv) )
