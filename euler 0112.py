def isInc(num):
        p = 0
        for c in str(num):
                if int(c) < p:
                        return False
                p = int(c)
        return True

def isDec(num):
        p = 9
        for c in str(num):
                if int(c) > p:
                        return False
                p = int(c)
        return True

def isBouncy(num):
        return (not isInc(num)) and (not isDec(num))


targetPct = 0.99
count = 269
i = 539
while (count / i) < targetPct:
#for i in range(1, mrange + 1):
        if isBouncy(i):
                count += 1

        if i == 21780:
                print(i, count, count / i)

        if (count / i) == targetPct:
                break
        
        i += 1

print(i)
