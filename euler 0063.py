
nums = set()
for n in range(1, 10**5):
        for p in range(1, 40):
                num = n**p
                if (p) == len(str(num)):
                        nums.add(num)
                        print(n, p)

print(len(nums))
