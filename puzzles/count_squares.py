import math
def countSquares(N):
	val = math.floor(math.sqrt(N))
	if(val == math.sqrt(N)):
		return val - 1
	else:
		return val

T = input()
ans = []

for i in range(T):
	ans.append(countSquares(input()))

for a in ans:
	print(a)