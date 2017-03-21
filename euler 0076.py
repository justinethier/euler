# start by summing 1's
# increase "left hand" number by 1 each iteration
# move on to 2's next, etc
#def fact(num):
#    if num <= 1:
#        return 1
#    return num * fact(num - 1)
#
sums = set()
iters = [0]

def start_find_sums(num):
    sums.clear()
    iters[0] = 0
    find_sums([1] * num, num)
    print(num, len(sums)-1, iters[0], len(sums) / iters[0])
        
def find_sums(data, num):
    if True: #data[0] < num and sum(data) == num:
        temp = list(data)
        temp.sort()

        iters[0] = iters[0] + 1
        if not str(temp) in sums:
            sums.add(str(temp))
            #print(len(sums))#

            for i in range(0, len(data)-1):
                data2 = list(data)
                data2[i] = data2[i] + data2.pop()
                find_sums(data2, num)

#find_sums([1] * 5, 5)

#for i in range(5,20):
#    start_find_sums(i)
#
#start_find_sums(100)

#sums = set()

def add_sum(sums, data):
    temp = list(data)
    temp.sort()
    if not str(temp) in sums:
        sums.add(str(temp))
        print(data)
        return True
    return False

def fast_find_sums(n):
    sums = set()
    last  = []
    cur = []
    
    for i in range(n-1, 0, -1):
        for l in last:
            lst = l[1:]
            lst.insert(0, i)
            lst[1] = lst[1] + 1
            if add_sum(sums, lst):
                cur.append(lst)    
                reduce_sum(sums, cur, lst, i, n)
        lst = [1]*(n-i)
        lst.insert(0, i)
        add_sum(sums, lst)
        cur.append(lst)

        last = cur
        cur = []

    return sums

# TODO: this may need to take into account bigger numbers
# such as 2, etc. compare with results at more than 7 iterations

# currently reduces list by stripping a 1 off the end of the list
# and adding to another list element
def reduce_sum(sums, cur, l, i, n):
    if (l[-1] > 1 or not 1 in l):
        return

    lst = l[:-1]

    if 1 in lst:
        offset = lst.index(1)
    else:
        offset = len(lst) - 1
        
    lst[offset] = lst[offset] + 1
    if sum(lst) > n:
        return
    if add_sum(sums, lst):
        cur.append(lst)    
        reduce_sum(sums, cur, lst, i, n)

s = fast_find_sums(12)
print(len(s))
#missing [1,2,2,2] and [2,2,3]
find_sums([1] * 12, 12)

print(sums - s)
