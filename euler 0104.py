def isPan(n):
 #   s = 0
 #   for c in n:
#        s += ord(c)
#
    #return s == 477
    
    l = list(n)
    l.sort()
    return l == ['1','2','3','4','5','6','7','8','9']


f = [1, 1, 2]

for i in range(4, 10**4):
    f[0], f[1], f[2] = f[1], f[2], f[1] + f[2]
    #print(f[2])

    s = str(f[2])
    l = len(s)
    if l > 18:
        start = s[0:9]
        end = s[l-9:]

        if (isPan(start)): # and isPan(end)):
            print(i)
            break
#print(i)
