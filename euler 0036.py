
# is pal in base 10 and 2
def isPalBase(n):
    b10 = str(n)
    b2 = bin(n)[2:]
    return isPal(b10) and isPal(b2)

# is number palindrome
def isPal(s):
    return (str(s) == str(s)[::-1])

sum = 0
for n in range(0, 10**6):
    if isPalBase(n):
        sum = sum + n

print(sum)
