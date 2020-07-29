import math

def nthRoot(N, M):
	for i in range(0, int(math.sqrt(M)) + 1):
		if pow(i, N) == M:
			return i
	return -1 


T = input()
ans = []

for i in range(T):
	inputs = raw_input().split(" ")
	ans.append(nthRoot(int(inputs[0]), int(inputs[1])))

for a in ans:
	print(a)