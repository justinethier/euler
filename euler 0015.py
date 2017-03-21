"""
Solution to Euler problem #15
All combinations for 2x2 board:

6
RRDD
RDRD
RDDR
DRRD
DRDR
DDRR


Bottom line, for an x-by-x board, the path must include
x R's (moves to the right) and x D's (moves down). So to
find the number of routes is to find all possible unique
orderings of R's and D's. Each ordering will be of length 2x.


"""

# This is a simple back-tracking algorithm, but does not scale.
# Just provided here to verify that the quicker solution is correct.
def countMoves(nRight, nDown):
    if nRight == 0 and nDown == 0:
        return 1
    elif nRight == 0 and nDown > 0:
        # only move down
        return countMoves(nRight, nDown - 1)
    elif nRight > 0 and nDown == 0:
        # only move right
        return countMoves(nRight - 1, nDown)
    else:
        # recurse right and down
        return countMoves(nRight - 1, nDown) + countMoves(nRight, nDown - 1)

for i in range(2, 10):
    print( countMoves(i, i) )

# Factorial used in real solution
def fact(n):
    mul = 1
    for i in range (1, n+1):
        mul = mul * i
    return mul

"""
Real solution that uses probability formula from
http://talkstats.com/showthread.php?p=5048

"
If there are n items and r of them are alike(nondistiguishable), the different no. of arrangements of these n items will be n! / r! where n!=1.2.3...n
For example if there are four letters A,B,C,D then different no. of arrangements will be
4!=1.2.3.4=24. But if two of them are alike, ie if the letters are A,A,B,C then the different no. of arrangements will be reduced to 4! / 2! because now no need to consider the internal arrangements of two A's.
In your example, the no. of different arrangements will be 6! /(3!*2!), since there are three A's and two B's.
"

"
Thank you very much, that does make sense 
So, to make sure I understand it ... if the letters were AABCCCDD, then the unique combinations would be:
8! / (2!*3!*2!) since there are 2 A's, 3 C's and 2 D's?
"

"""
for i in range(2, 21):
    solution = fact(i * 2) / (fact(i) * fact(i))
    print (solution)
