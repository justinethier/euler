
digits = str(2**1000)
sum = 0

for i in range(0, len(digits)):
    sum = sum + int(digits[i])

print(sum)
