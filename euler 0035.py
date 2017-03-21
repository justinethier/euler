def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def int2list(n):
    result = []
    for c in str(n):
        result.append(c)
    return result

def rotations(l):
    yield(l)
    for i in range(1, len(l)):
        head = l[0]
        l = l[1:]
        l.append(head)
        yield(l)
        
#import itertools

cprimes = set()
for n in range(0, 10**6):
    if isprime(n):
        allprime = True
        for x in rotations(int2list(n)):
            if not isprime(int("".join(x))):
                allprime = False
                break
        if allprime:
            cprimes.add(n)

print(len(cprimes))
