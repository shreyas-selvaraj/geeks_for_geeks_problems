def reverse(arr):
	hp = 0
	tp = len(arr) - 1

	while(hp < tp):
		temp = arr[hp]
		arr[hp] = arr[tp]
		arr[tp] = temp
		hp += 1
		tp -= 1
	return arr


T = input()
ans = []

for i in range(T):
	N = input()
	inputs = raw_input().split(" ")
	ans.append(reverse(inputs))

for a in ans:
	print(a)
