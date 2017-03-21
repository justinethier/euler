#
# Solution to project euler #31 - Combinations of English currency
#
# by Justin Ethier, March 2010
#
Denom = [1, 2, 5, 10, 20, 50, 100, 200]

def find(iCoin, cSum):
    '''
    Recursive function to finds the number of solutions to
    the multivariable equation

    200n + 100m + ...

    Where n, m, etc is:
    
    [0-1]200 + [0-2]100 + [0-4]50 + ...
    range of any variable is 0-c/200 where c is the constant

    The function uses backtracking to evaluate possible combinations,
    and terminate a branch if the sum becomes too large.
    '''
    nSolutions = 0
    if (iCoin >= len(Denom)): # Base case, no more denominations left
        return nSolutions
    
    for i in range(0, int(200 / Denom[iCoin]) + Denom[iCoin]):
        value = cSum + i * Denom[iCoin]
        if value > 200:
            return nSolutions # Summation too large, terminate this branch
        elif value == 200:
            #print(i)
            nSolutions += 1
        else:
            # Search with smaller denominations
            nSolutions += find(iCoin + 1, value)

    return nSolutions

print( find(0, 0) )
