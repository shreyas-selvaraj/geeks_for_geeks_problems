import math

def reverse_digits(N):
	#get digits no reverse, get rid of trailing zeroes before reverse or leading after 
	digits = []
	for i in range(0, int(math.log(N, 10)) + 1):
		digits.append(N // pow(10, i) % 10)

	#already in reverse order, don't need to reverse
	while(digits[0] == 0):
		digits.pop(0)

	string = ""
	for digit in digits:
		string = string + str(digit)

	ans.append(int(string))

T = input()
ans = []

for i in range(T):
	N = input()
	reverse_digits(N)

for i in ans:
	print(i)