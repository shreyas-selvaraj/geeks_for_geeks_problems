def gcd(a, b):
	if(a == b):
		return a
	dif = abs(b - a)
	max_num = max(a,b)
	while(max_num > dif):
		max_num = max_num - dif

	for i in range(max_num, 0, -1):
		if a % i == 0 and b % i == 0:
			ans.append(i)
			break

T = input()
ans = []

for i in range(T):
	string = raw_input().split(" ")
	gcd(int(string[0]), int(string[1]))

for a in ans:
	print(a)
