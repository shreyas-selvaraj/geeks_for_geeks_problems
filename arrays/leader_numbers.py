def leaders(arr):
	#start from back of array, last place is leader, if number to left is bigger than current 
	#leader then add to leaders 

	leaders = [arr[len(arr) - 1]]
	currLeader = arr[len(arr) - 1]
	for i in range(len(arr) - 2, -1, -1):
		if(arr[i] >= currLeader):
			leaders.append(arr[i])
			currLeader = arr[i]
	return leaders

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	arr = [int(x) for x in arr]
	ans.append(leaders(arr))

for a in ans:
	print(a)
