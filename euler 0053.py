# Solution to project euler 53
#
#    find all fact from 1-100
#    cache them
#    then brute force using this data
#
# Solution completes very quickly
#

# Cache factorials
fac = [1]
for n in range(1, 101):
    fac.append(fac[n-1] * n)

def nCr(n, r):
    return fac[n] / (fac[r] * fac[n - r])

count = 0
for n in range(10, 101):
    for r in range(1, n):
        if nCr(n, r) > 10**6:
            count += 1

print(count)
