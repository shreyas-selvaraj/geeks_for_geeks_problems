def max_index(arr):
	max_dif = 0
	for i in range(0, len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if(arr[j] >= arr[i]):
				if(j - i > max_dif):
					max_dif = j - i
	return max_dif

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	ans.append(max_index(arr))

for a in ans:
	print(a)