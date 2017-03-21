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

nums = primes(2000000)
sum = 0
for x in nums:
    sum = sum + x

print(sum)
