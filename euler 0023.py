def pdivs(n):
    result = []
    for i in xrange(1, int(n/2)+1):
        if n % i == 0:
            result.append(i)
    return result

print(sum(pdivs(28)))

#abundant = []
#for i in range(12, 28124):
#    if sum(pdivs(i)) > i:
#           abundant.append(i)

lookup = {}
for n in abundant:
    lookup[n] = n

result = []
for n in xrange(1, 28124):
    found = False
    for ai in xrange(0, len(abundant)):
        if abundant[ai] >= n:
            break;

        if (n - abundant[ai]) in lookup:
            found = True
            break

    if not found:
        result.append(n)
