def int2str(n):
    if n < 20:
        return ((["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"])[int(n)])

    elif n < 100:
        l = ((["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"])[int(n / 10)])

        if (n % 10) > 0:
            l += int2str(n % 10)
            
        return l

    elif n < 1000:
        if (n % 100) == 0:
            l  = int2str(n / 100)
            l += ("hundred")

        else:
            l  = int2str(n / 100)
            l += ("hundredand")
            l += int2str(n % 100)

        return l

    return ("onethousand")

s = 0
for n in range(1, 1001):
    s += len(int2str(n))
    print(n, int2str(n))
print(s)
