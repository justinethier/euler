'''
Solution to Project Euler #97
http://projecteuler.net/index.php?section=problems&id=97

Python makes this one too easy! :)
'''
a = 2 ** 7830457
b = a * 28433
print(b % 10000000000 + 1)
