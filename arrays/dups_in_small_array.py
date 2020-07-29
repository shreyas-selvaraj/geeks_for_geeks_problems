def find_dups(arr):
	#use hash table, if occurance in add to array of nums 
	d = {}
	dups = []
	for i in range(0, len(arr)):
		if arr[i] not in d:
			d[arr[i]] = 1
		else:
			dups.append(arr[i])

	if(len(dups) == 0):
		dups.append(-1)
	return dups

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	ans.append(find_dups(arr))

for a in ans:
	print(a)