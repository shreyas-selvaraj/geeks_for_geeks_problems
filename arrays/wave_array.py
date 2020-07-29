def wave(arr):
	for i in range(0, len(arr) - 1, 2):
		temp = arr[i]
		arr[i] = arr[i + 1]
		arr[i + 1] = temp
	return arr

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	arr = [int(x) for x in arr]
	ans.append(wave(arr))

for a in ans:
	print(a)