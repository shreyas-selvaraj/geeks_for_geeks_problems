from fractions import Fraction

def pair_cube(N):
	from fractions import Fraction
	power = Fraction("1/3")
	counter = 0
	m = int(pow(N, power)) + 1
	for a in range(1, m):
		for b in range(0, int(pow(N, power)) + 1):
			if pow(a, 3) + pow(b, 3) == N:
				counter += 1
	return counter 

T = input()
ans = []

for i in range(T):
	ans.append(pair_cube(input()))

for a in ans:
	print(a)