'''
Solution to Project Euler problem #33
http://projecteuler.net/index.php?section=problems&id=33
'''
mul = 1.0

for n in range (10, 100):
    for d in range (10, 100):
        #if (d % 10) > 0 and ((n / d) == ( int(n / 10) / (d % 10) )):
        #    print(n, d)

        na = int(n / 10)
        da = d % 10

        if (na == da) and ((n / d) == (n % 10) / int(d / 10)):
            if (n % 11) != 0: # get rid of trivial cases
                print(n, d)

                mul *= (n / d)

print("Solution: ", mul)
