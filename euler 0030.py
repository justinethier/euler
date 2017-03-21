for n in range(2, 10**6):
    sum = 0
    for d in str(n):
        sum = sum + int(d, 10)**5
    if n == sum:
        print(sum)
