
fact = [1, 1, 2, 6, 24,120,720,5040,40320,362880]

#def fact(n):
#    if n == 1:
#        return 1
#    else:
#        return n * fact(n-1)

for n in range(3, 10**5):
    sum = 0
    for d in str(n):
        sum = sum + fact[int(d, 10)]
    if n == sum:
        print(sum)
