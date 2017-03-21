
def digitalSum(n):
    sum = 0
    for digit in str(n):
        sum = sum + int(digit)

    return sum

#digitalSum
maxSum = 0
for a in range(1, 100):
    for b in range(1, 100):
        s = digitalSum(a ** b)
        if s > maxSum:
            maxSum = s

print(maxSum)
