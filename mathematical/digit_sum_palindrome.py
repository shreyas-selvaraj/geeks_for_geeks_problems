import math

def isSumPal(N):
	#store digits in array, check if forward and reverse equal
	s = 0
	digits = []
	for i in range(0, int(math.log(N, 10)) + 1):
		s = s + N // pow(10, i) % 10

	for j in range(0, int(math.log(s, 10)) + 1):
		digits.append(s // pow(10, j) % 10)

	if digits == digits[::-1]:
		ans.append(True)
	else:
		ans.append(False)

T = input()
ans = []

for i in range(T):
	N = input()
	isSumPal(N)

for a in ans:
	print(a)