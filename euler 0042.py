def findTri(n):
    tri = {}
    for i in range(1, n):
        tri[int( (i * (i+1)) / 2)] = True
    return tri

def tri(word):
    sum = 0
    for c in word:
        sum = sum + ord(c) - 64
    return sum

triNums = findTri(1000)

f = open("words.txt", "r")
words = f.readlines()[0].split(",")
f.close()

count = 0
for word in words:
    word = word.strip('"')
    num = tri(word)
    if num in triNums:
        count = count + 1

print(count)
