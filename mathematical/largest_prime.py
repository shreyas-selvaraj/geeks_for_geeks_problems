def largest_prime(N):
	#using sieve of e
	isPrime = [True for x in range(N + 1)]
	p = 2

	while(p * p <= N):
		if(isPrime[p] == True):
			for i in range(p * 2, N + 1, p): #every multiple of p
				isPrime[i] = False
		p += 1

	isPrime[0] = False
	isPrime[1] = False

	for index in range(len(isPrime) - 1, -1, -1):
		if isPrime[index] == True and N % index == 0:
			ans.append(index)
			break


T = input()
ans = []

for i in range(T):
	largest_prime(input())

for a in ans:
	print(a)