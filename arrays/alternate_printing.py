def alt_print(arr):
	temp = []
	for i in range(0, len(arr), 2):
		temp.append(arr[i])
	return temp

T = input()
ans = []

for i in range(T):
	N = input()
	inputs = raw_input().split(" ")
	ans.append(alt_print(inputs))

for a in ans:
	for num in a:
		print(num),
	print