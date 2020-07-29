import math
def isPerfect(N):
	s = 0
	for i in range(1, N):
		if N % i == 0:
			s += i

	if s == N:
		return 1
	else:
		return 0

T = input()
ans = []

for i in range(T):
	ans.append(isPerfect(input()))

for a in ans:
	print(a)