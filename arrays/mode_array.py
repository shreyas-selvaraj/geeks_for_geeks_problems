def mode(arr):
	#could sort and check
	#dictionary

	occurances = {}
	for i in arr:
		if i not in occurances.keys():
			occurances[i] = 1
		else:
			occurances[i] += 1

	maxVal = 0
	mode = 0
	for key in occurances.keys():
		if(occurances[key] > maxVal):
			maxVal = occurances[key]
			mode = key
	return mode

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	ans.append(mode(arr))

for a in ans:
	print(a)