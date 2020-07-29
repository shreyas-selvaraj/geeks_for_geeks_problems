def lcm(a, b):
	for i in range(max(a,b), a * b + 1):
		if i % a == 0 and i % b == 0:
			return i

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

T = input()
ans = []

for i in range(T):
	inputs = raw_input().split(" ")
	ans.append(lcm(int(inputs[0]), int(inputs[1])))
	ans.append(gcd(int(inputs[0]), int(inputs[1])))

for i in range(0, len(ans)):
	if(i % 2 == 0 and i > 0):
		print
	print(ans[i]),