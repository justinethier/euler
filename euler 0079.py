
def addToPasscode(num, order, passcode):
    if len(passcode) == 0:
        #empty list
        return [num]
    elif passcode.count(num) > 0:
        #already part of passcode
        return passcode

    # find last slot (0-2) that the number is used in
    # must place num before any members of slots to right
    # must place num after any members of slots to the left
    for i in range(0, len(passcode)):
        if not (passcode[i] in (order[num]['before'])):
            if passcode[i] in order[num]['after']:
                passcode.insert(i, num)
                print(passcode)
                return passcode            
            else:
                passcode.insert(i+1, num)
                print(passcode)
                return passcode

    # add to end of the list
    passcode.append(num)
    print(passcode)
    return passcode

order = {}
f = open('keylog.txt', 'r')

# Build a before and after list for each num
for line in f.readlines(): #["319","680","180"]:
    a, b, c = int(line[0]), int(line[1]), int(line[2])
    if not a in order: order[a] = {'before': set(), 'after': set()}
    if not b in order: order[b] = {'before': set(), 'after': set()}
    if not c in order: order[c] = {'before': set(), 'after': set()}

    print(a,b,c)
    order[a]['after'].add(b)
    order[a]['after'].add(c)

    order[b]['before'].add(a)
    order[b]['after'].add(c)

    order[c]['before'].add(a)
    order[c]['before'].add(b)
print(order)

passcode = []
f = open('keylog.txt', 'r')
for line in f.readlines(): #["319","680","180"]:
    for i in range(0, 3):
        passcode = addToPasscode(int(line.strip()[i]), order, passcode)


print(passcode)

