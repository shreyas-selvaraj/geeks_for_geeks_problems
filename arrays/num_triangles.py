def num_triangles(arr):
	#for each pair of two numbers count number of remaining numbers that are greater than sum
	s = 0
	counter = 0
	for i in range(0, len(arr) - 1):
		for j in range(i + 1, len(arr)):
			s = arr[i] + arr[j]
			for z in range(j + 1, len(arr)):
				if(z < s):
					counter +=1
	return counter

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	ans.append(num_triangles(arr))

for a in ans:
	print(a)
