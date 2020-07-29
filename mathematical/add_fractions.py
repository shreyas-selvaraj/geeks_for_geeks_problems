def gcd(a, b):
	if a == b:
		return a 
	dif = abs(b - a)
	max_num = max(a,b)
	while(max_num > dif):
		max_num = max_num - dif

	for i in range(max_num, 0, -1):
		if a % i == 0 and b % i == 0:
			return i
			break

def add(num1, den1, num2, den2):
	#only add sequence of num and den to ans
	denf = den1 * den2
	numf = num1 * den2 + num2 * den1
	cd = gcd(numf, denf)
	numf /= cd
	denf /= cd
	ans.append(numf)
	ans.append(denf)

T = input()
ans = []

for i in range(T):
	inputs = raw_input().split(" ")
	add(int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]))

for i in range(0, len(ans)):
	if(i % 2 == 1):
		print("/"),
		print(ans[i])
	else:
		print(ans[i]),