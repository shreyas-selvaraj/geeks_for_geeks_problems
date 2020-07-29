def max_sum_path(arr1, arr2):
	minimum = min(len(arr1), len(arr2))
	maximum = max(len(arr1), len(arr2))
	s = 0
	ptr = 0

	while(ptr < minimum):
		s += max(arr1[ptr], arr2[ptr])
		ptr += 1

	if(len(arr1) <= len(arr2)):
		for i in range(minimum, maximum):
			s += arr2[i]

	if(len(arr1) > len(arr2)):
		for i in range(minimum, maximum):
			s += arr1[i]
	return s


T = input()
ans = []

for i in range(T):
	N = raw_input()
	arr1 = [int(x) for x in raw_input().split(" ")]
	arr2 = [int(x) for x in raw_input().split(" ")]
	ans.append(max_sum_path(arr1, arr2))

for a in ans:
	print(a)