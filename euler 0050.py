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

max_count = 0
max_prime = 0

nums = primes(10**6)
snums = set(nums)
for i in range(0, 100):
     for ii in range(i+1, len(nums)+1):
             s = sum(nums[i:ii])

             if s > nums[-1]:
                     break
                
             if s in snums and ii-i > max_count:
                     max_prime = s
                     max_count = ii - i
                     temp = (ii, i)
                                     
print(max_count, max_prime, temp)
