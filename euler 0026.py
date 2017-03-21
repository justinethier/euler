
def numFractionalDigits(divisor):
    """
    """
    cycleLength = 0
    digits = "0." # only req'd for display purposes, may be commented out below
    remainder = 1
    states = []
    
    while True:
        dividend = remainder * 10
        quotient = dividend / divisor
        remainder = dividend % divisor
        currentState = (quotient, remainder, dividend)

        digits = digits + str(quotient)  # method may only be Temporary!
        if remainder == 0:
            break
        elif len(states) > 1000:
            print("Maximum number of digits detected (100), assuming no cycle for " + str(divisor))
            break;
        elif currentState in states:
            # If a state is repeated then a cycle has just ended
            idx = states.index(currentState) + 2 # Index of first decimal digit in string
            digits = digits[:idx] + "(" + digits[idx:-1] + ")"
            cycleLength = len(states) - states.index(currentState)
            break

        states.append(currentState)

    #print(digits)
    #print(cycleLength)
    return cycleLength

d, count = -1, -1
for i in range(2, 1001):
    icount = numFractionalDigits(i)
    if icount > count:
        d, count = i, icount
print d, count
