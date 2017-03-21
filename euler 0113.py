# test code:
def isInc(num):
        p = 0
        for c in str(num):
                if int(c) < p:
                        return False
                p = int(c)
        return True

# brute-force algorithm
def isBouncy(n):
        num = str(n)
        isInc, isDec = True, True
        for i in range(1, len(num)):
                if num[i - 1] > num[i]: isInc = False
                if num[i - 1] < num[i]: isDec = False
                if (not isInc) and (not isDec): return True
        return False


# TODO: brute-force approach will not scale
# another approach - as non-bouncy numbers are sparse, how about
# trying to generate them using existing list of non-bouncy numbers.
# probably can just take a non-bouncy number and add a digit at the
# end for each number that is applicable (EG: add 1, 0 to end of 664432
# to create 2 new bouncy numbers in 10**6 range)

# iter 3 - 165
# 45 + 45-9 + 45-9-8 + 45-9-8-7 + 45-9-8-7-6 + 45-9-8-7-6-5 + 45-9-8-7-6-5-4 + 45-9-8-7-6-5-4-3 + 45-9-8-7-6-5-4-3-2

# iter 4 - 495
#1 + (3 + 1) + (6 + 3 + 1) + (10 + 6 + 3 + 1) + (15 + 10 + 6 + 3 + 1) + (21 + 15 + 10 + 6 + 3 + 1) + (28 + 21 + 15 + 10 + 6 + 3 + 1)+ (36 + 28 + 21 + 15 + 10 + 6 + 3 + 1) + (45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1)

# iter 5 - 3003
#1 + (3 + 1) + (6 + 3 + 1) + (10 + 6 + 3 + 1) + (15 + 10 + 6 + 3 + 1) + (21 + 15 + 10 + 6 + 3 + 1) + (28 + 21 + 15 + 10 + 6 + 3 + 1)+ (36 + 28 + 21 + 15 + 10 + 6 + 3 + 1) + (45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1)


#count = 0 #12951
#for i in range(10**3, 10**4):
#        if isInc(i): #not isBouncy(i):
#                count += 1
#print(count)

cur = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Values from iter 2
for iter in range(3, 6): # 10**iter
        nxt = [1]*9
        for i in range(0, 9):
                nxt[i] = sum(cur[:i+1])
        cur = list(nxt)
        
