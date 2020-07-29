def convert(N):
	# n as string
	decimal = 0
	for i in range(0, len(N)):
		if N[i] == "1":
			decimal = decimal + pow(2, (len(N) - 1 - i)) #because of way string is indexed
	ans.append(decimal)

T = input()
ans = []

for i in range(T):
	convert(raw_input())

for a in ans:
	print(a)