def tri(n):
    return int( (n * (n + 1)) / 2 )

def pent(n):
    return int( (n * (3 * n - 1)) / 2 )

def hexa(n):
    return int( (n * (2 * n - 1) ) )

nt = {}
pt = {}
hx = {}
for i in range(143, 100000):
    nt[ i ] = tri(i)
    pt[ pent(i) ] = True
    hx[ hexa(i) ] = True

i = 286
while i < 100000:
    if nt[i] in pt and nt[i] in hx:
        print( nt[i] )
        break
    i = i + 1
