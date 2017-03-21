# Solution to Project Euler #57
#
# by Justin Ethier
#

class fract():
    '''
    Class representing a fraction,
    with operations required by this problem.
    '''
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    def add(self, n):
        self.num += (n * self.denom)
    def inv(self):
        ''' Invert, IE divide by one '''
        self.num, self.denom = self.denom, self.num
    def print(self):
        print(self.num, self.denom)
    def solution(self):
        return len(str(self.num)) > len(str(self.denom))

def calc(i):
    ''' Calculate iteration i'''
    f = fract(1,2)
    for i in range(i):
        f.add(2)
        f.inv()
        
    f.add(1)
    return f

solutions = [f for f in range(1000) if calc(f).solution()]
print( len(solutions) )
