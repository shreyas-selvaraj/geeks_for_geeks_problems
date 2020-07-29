def factorial(N):
	if N == 1 or N == 0:
		return 1 
	return N * factorial(N - 1)

T = input()
ans = []

for i in range(T):
	ans.append(factorial(input()))

for a in ans:
	print(a)