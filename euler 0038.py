
def is_pandigital(n):
        l = list(n)
        l.sort()
        for i in range(0, len(l)):
                if l[i] != str(i+1):
                        return False
        return True


def calc(n, s):
        result = ""
        for i in range(1, s+1):
                result += str(i * n)
        return result

cand = ""
for n in range(1, 10**6):
        for p in range(1, 10):
                x = calc(n, p)
                if (len(x) > len(cand)) or (len(x) == len(cand) and x > cand):
                        if is_pandigital(x):
                                cand = x

print(cand)
