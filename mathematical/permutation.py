def factorial(N):
	if N == 1 or N == 0:
		return 1 
	return N * factorial(N - 1)

def nPr(n, r):
	ans.append(factorial(n)/factorial(n-r))

T = input()
ans = []

for i in range(T):
	inputs = raw_input().split(" ")
	nPr(int(inputs[0]), int(inputs[1]))

for a in ans:
	print(a)