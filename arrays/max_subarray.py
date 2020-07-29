def max_subarray(arr):
	#subarray determined by negative numbers 
	# curr_s = 0
	# max_s = 0
	# s_index = 0
	# e_index = 0
	# dif = 0
	# for i in range(len(arr)):
	# 	if(arr[i] < 0 or i == len(arr) - 1):
	# 		if(curr_s > max_s):
	# 			e_index = i - 1
	# 			dif = e_index - s_index
	# 			s_index = i + 1
	# 		if(curr_s == max_s and max_s != 0):
	# 			if(i - 1 - s_index > dif):
	# 				e_index = i - 1
	# 				dif = i - 1 - s_index
	# 				s_index = i + 1

	# 	curr_s += arr[i]

	# return arr[e_index - dif : e_index]

	#above is more effective but more complicated 
	subarrays = []
	s_index = 0
	for i in range(len(arr)):
		if(arr[i] < 0):
			subarrays.append(arr[s_index : i])
			s_index = i + 1
		if (i == len(arr) - 1):
			subarrays.append(arr[s_index : len(arr)])

	curr_max = 0
	curr_dif = 0
	curr_s = 0
	max_subarray = []
 	for subarray in subarrays:
		for num in subarray:
			curr_s += num
		if(curr_s > curr_max):
			curr_max = curr_s
			curr_dif = len(subarray)
			max_subarray = subarray
		if(curr_s == curr_max):
			if(len(subarray) > curr_dif):
				max_subarray = subarray
		curr_s = 0
	return subarray

T = input()
ans = []

for i in range(T):
	N = input()
	arr = raw_input().split(" ")
	arr = [int(x) for x in arr]
	ans.append(max_subarray(arr))

for a in ans:
	print(a)