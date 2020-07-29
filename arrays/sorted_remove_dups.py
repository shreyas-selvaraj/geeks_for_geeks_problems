def remove_dups(arr):
	prev = arr[0]
	temp = [prev]
	for i in range(1, len(arr)):
		if(arr[i] != prev):
			prev = arr[i]
			temp.append(arr[i])
	return temp

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	ans.append(remove_dups(arr))

for a in ans:
	print(a)
