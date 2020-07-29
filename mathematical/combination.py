def factorial(N):
	if N == 1 or N == 0:
		return 1 
	return N * factorial(N - 1)

def nCr(n, r):
	numerator = 1
	for i in range(n, n-r, -1):
		numerator *= i
	ans.append(numerator/factorial(r))

T = input()
ans = []

for i in range(T):
	inputs = raw_input().split(" ")
	nCr(int(inputs[0]), int(inputs[1]))

for a in ans:
	print(a)