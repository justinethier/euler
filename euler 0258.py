
# Given k, determine what number range it falls into in sequence
# for example,
#  dr(1000) = (0, 1999)
#  dr(9999) = (8000, 9999)
def dr(k):
    low = k - (k % 2000)
    return (low, low + 1999)

# find cache index for k
def ci(k):
    return k - (k%2000)

class Buffer:
    def __init__(self):
        self.cache = [{}, {}]
        self.active = 0
        self.buffer_size = 500000
        
    def cadd(self, k, val):
        if len(self.cache[self.active]) > self.buffer_size:
            self.cache[1 - self.active] = {}
            self.active = 1 - self.active
        self.cache[self.active][k] = val
        
    def cget(self, k):
        if (k in self.cache[self.active]):
            return self.cache[self.active][k]
        return self.cache[1 - self.active][k] # return from inactive buffer

    def cfind(self, val):
        if (val in self.cache[self.active]):
            return True
        return val in self.cache[1 - self.active]
    #def ret(self):
    #    return self.cache[self.active]

c = Buffer()

def fast_g(k):
    if (k <= 1999):
        c.cadd(k, 1)
        return c.cget(k)
    elif c.cfind(k):
        return c.cget(k)

    if not c.cfind(k - 1999):
        c.cadd(ci(k - 1999), fast_g(ci(k - 1999)) % 20092010)

    if not c.cfind(k - 2000):
        c.cadd(ci(k - 2000), fast_g(ci(k - 2000)) % 20092010)
        #cache[active][ci(k - 2000)] = fast_g(ci(k - 2000)) # index fast_g?

    return c.cget(ci(k - 2000)) + c.cget(ci(k - 1999)) % 20092010

# driver for fast_g to avoid recursion problems at large k
i = 10**5
for k in range(0, 10**10, 10**6):
#    if (i == k):
#        print(i)
#        i = 10**(k+1)
        
    temp = fast_g(k)
    
#print(fast_g(10**8))

# Slow function, useful for testing at low values of k
def g(k):
    if (k <= 1999):
        return 1
    return g(k - 2000) + g(k - 1999)

def fib(k):
    if (k <= 1):
        return k
    return fib(k - 1) + fib(k - 2)
