def hasThreeDivisors(N):
	# 1 and number itself counts as divisor
	counter = 0
	for i in range(1, N + 1):
		if N % i == 0:
			counter += 1
	if(counter == 3):
		return True
	else:
		return False

def runner(N):
	#return number of numbers that have 3 divisors
	counter = 0
	for i in range(4, N + 1):
		if hasThreeDivisors(i):
			counter += 1
	return counter


T = input()
ans = []

for i in range(T):
	ans.append(runner(input()))

for a in ans:
	print(a)