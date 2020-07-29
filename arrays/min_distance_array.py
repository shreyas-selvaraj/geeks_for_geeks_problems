def min_dist(arr, x, y):
	x_indeces = []
	y_indeces = []

	for i in range(len(arr)):
		if(arr[i] == x):
			x_indeces.append(i)
		if(arr[i] == y):
			y_indeces.append(i)

	if(len(x_indeces) == 0 or len(y_indeces) == 0):
		return -1

	else:
		return abs(min(y_indeces) - min(x_indeces))

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	x,y = raw_input().split(" ")
	ans.append(min_dist(arr, x, y))

for a in ans:
	print(a)