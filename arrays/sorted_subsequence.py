def num_sequences(arr):
	#size subsequence is 3
	#sorted subseqence
	num = 0
	for i in range(0, len(arr) - 2):
		for j in range(i + 1, len(arr) - 1):
			for k in range(j + 1, len(arr)):
				if(arr[k] > arr[j] and arr[j] > arr[i]):
					num += 1
	return num

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	arr = [int(x) for x in arr]
	ans.append(num_sequences(arr))

for a in ans:
	print(a)