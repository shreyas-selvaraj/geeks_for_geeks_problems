def findKth(a, b, i):
	val = pow(a, b)
	ans.append(val // pow(10, i - 1) % 10)

T = input()
ans = []

for i in range(T):
	string = raw_input().split(" ")
	findKth(int(string[0]), int(string[1]), int(string[2]))

for a in ans:
	print(a)