def pair_with_sum(arr, s):
	pairs = []
	for i in range(0, len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if(arr[i] + arr[j] == s):
				pairs.append((arr[i], arr[j]))

	if(len(pairs) == 0):
		return -1
	else:
		return pairs

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	s = input()
	ans.append(pair_with_sum(arr, s))

for a in ans:
	print(a)