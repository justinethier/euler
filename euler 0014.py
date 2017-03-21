def collatz(n):
    iter = 0
    while n > 1:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = 3 * n + 1

        iter = iter + 1

    return iter


num, iterations = 0,0

for i in range(1, 1000000):
    iter = collatz(i)

    if iter > iterations:
        num, iterations = i, iter

print(num, iterations)
