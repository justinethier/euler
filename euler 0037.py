def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=list(range(3,n+1,2))
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			#print(int(j))
			if int(j) < len(s): s[int(j)]=0
			while j<half:
				#print(int(j))
				if int(j) < len(s): s[int(j)]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def is_lr_rl_trunc(n, primes):
        num = str(n)
        # left-to-right
        for i in range(0, len(num)):
                #print(num[i:])
                if not int(num[i:], 10) in primes:
                        return False
        # right-to-left
        for i in range(1, len(num)):
                #print(num[:i])
                if not int(num[:i], 10) in primes:
                        return False                
        return True

tlist = []
nums = primes(4000000)
nums_set = set(nums)
#is_lr_rl_trunc(3797, nums)

for i in range(4, len(nums)):
        if is_lr_rl_trunc(nums[i], nums_set):
                print(nums[i])
                tlist.append(nums[i])      
        
