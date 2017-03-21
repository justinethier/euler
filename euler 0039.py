maxs = [[], 0]

for p in range(120, 1001):
    s = []
    for a in range(1, int(p/2)):
        for b in range(a, int(p/2)):
            c = p - a - b
            if (a**2 + b**2) == c**2:
                s.append( (a, b, c) )
                    
    if len(s) > len(maxs[0]):
        maxs = [s, p]
