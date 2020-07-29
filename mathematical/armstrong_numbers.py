import math

def isArmstrong(N):
	#divide by power of ten then take modulo of ten
	s = 0
	for i in range(0, int(math.log(N, 10)) + 1):
		digit = (N // pow(10, i)) % 10
		s = s + pow(digit, 3)
	if(s == N):
		ans.append(True)
	else:
		ans.append(False)

T = input()
ans = []

for i in range(T):
	N = input()
	isArmstrong(N)

for i in ans:
	print(i)