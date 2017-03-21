def isPal(n):
    return str(n) == str(n)[::-1]

def isLychrel(n):
    for i in range(0, 50):
        n = n + int(str(n)[::-1])
        if isPal(n) == True:
            return False
    return True

count = 0
for i in range(0, 10000):
    if isLychrel(i):
        count = count + 1

print(count)
