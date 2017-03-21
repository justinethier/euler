def num2arr(n):
    arr = []
    for c in str(n):
        arr.append(c)
    arr.sort()
    return arr

for i in range(1, 10**7):
    if num2arr(i * 1) == num2arr(i * 2) and \
       num2arr(i * 2) == num2arr(i * 3) and \
       num2arr(i * 3) == num2arr(i * 4) and \
       num2arr(i * 4) == num2arr(i * 5) and \
       num2arr(i * 5) == num2arr(i * 6):
        print(i)
        break;
 
