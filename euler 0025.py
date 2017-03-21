def fib(terminator):
    x, y, z = 1, 1, 2
    term = 3
    
    while True:
        term = term + 1
        x, y, z = y, z, y + z
        if z >= terminator:
            return z, term #break

print(fib(10**2))
print(fib(10**1000))
