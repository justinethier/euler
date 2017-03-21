#tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
tri = []

f = open("triangle.txt", 'r')
for line in f.readlines():
    line = line.split(' ')
    for i in range(0, len(line)):
        line[i] = int(line[i])
    tri.append(line)
f.close()
print(tri)

# for each number in row n
for row in range(len(tri) - 1, 0, -1):
    #   look at two possible sums in row n-1
    #   choose largest sum, store it at this level
    for i in range(0, len(tri[row-1])):
        root = tri[row-1]
        leaf = tri[row]
        if leaf[i] > leaf[i+1]:
            root[i] = root[i] + leaf[i]
        else:
            root[i] = root[i] + leaf[i+1]
