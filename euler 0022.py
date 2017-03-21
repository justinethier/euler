def score(word):
    sum = 0
    for c in word.strip('"'):
        sum = sum + ord(c) - 64
    return sum

f = open("names.txt", "r")
names = f.readlines()[0].split(",")
f.close()
names.sort()

total = 0
for i in range(0, len(names)):
    total = total + (i + 1) * score(names[i])

print(total)
