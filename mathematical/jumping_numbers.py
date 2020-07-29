import math

def isJumping(N):
	for i in range(0, int(math.log(N, 10))):
		right_digit = (N // pow(10, i)) % 10
		left_digit = (N // pow(10, i + 1)) % 10
		if abs(right_digit - left_digit) == 1:
			return True

		else:
			return False
	return True


def printJumpingNumbers(N):
	print(0), 
	for i in range(1, N + 1):
		if isJumping(i):
			print(i),

T = input()
inputs = []

for i in range(T):
	inputs.append(input())

for i in inputs:
	printJumpingNumbers(i)
	print