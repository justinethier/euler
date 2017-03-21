result = 0,0,0

def isPalindrom(product):
    return str(product) == str(product)[::-1]
    
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y;
        
        if (isPalindrom(product) and product > result[0]):
            result = (product, x, y)

print(result)
