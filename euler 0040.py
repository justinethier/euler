# d1 - 1
# d10 - 1
# d100 - 5?
# d1000 -
# d10000 -
# d100000 -
# d1000000 -

# Find number at target index
#  target - Target index
#  idx - Index we are currently one
#  cur - Current number
#  curlen - # of digits in current number
def atIdx(target, idx, cur, curlen):
    if idx == target or (idx < target and idx + curlen-1 >= target):
        return int(str(cur)[target - idx])
    return None

targets, target, idx, cur = [], 1, 1, 1

while target <= 10**6:
    curlen = len(str(cur))

    nextDigit = atIdx(target, idx, cur, curlen)
    if nextDigit != None:
        print(target, nextDigit, idx, cur, curlen)
        
        targets.append(nextDigit)
        target *= 10

    cur += 1 # move to next number    
    idx = idx + curlen # increment index

# Multiply all digits in the result set
result = 1
for d in targets:
    result *= d
print(result)
