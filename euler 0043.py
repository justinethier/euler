# constraints -
# d4 - even
# d6 - (0, 5)
# d3,d4,d5 - must sum to 3,6, or 9


from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

# Determine if number has properties required by
# Euler 43. Do not check if pandigital as
# already done by this point
def is_valid(num):
    return (int(num[1:4])  %  2) == 0 and \
           (int(num[2:5])  %  3) == 0 and \
           (int(num[3:6])  %  5) == 0 and \
           (int(num[4:7])  %  7) == 0 and \
           (int(num[5:8])  % 11) == 0 and \
           (int(num[6:9])  % 13) == 0 and \
           (int(num[7:10]) % 17) == 0

if __name__=="__main__":
    #print("Permutations of 'love'")
    #for p in xpermutations(['l','o','v','e']): print(''.join(p))
    nsum = 0
    for n in xpermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        num = "".join(["%s" % v for v in n])
        #print(num)
        if is_valid(num):
            nsum = nsum + int(num)

print(nsum)
