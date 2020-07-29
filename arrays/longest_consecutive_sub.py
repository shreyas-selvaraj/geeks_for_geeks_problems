def longest_subsequence(arr):
	#sort then count?
	#hash, put arr to set
	#check if element is start of subsequence, element - 1 exists or not
	#if not then continue to check for next in subsequence updating length, do for all elements 
	d = {}
	s = set(arr)
	longest = 0
	
	#GOOD BECAUSE SEARCH IS ONLY O(1) for hash table
	for i in range(len(arr)):
		if(arr[i] - 1) not in s: #it is the beginning of a subsequence 
			j = arr[i]
			while(j in s):
				j += 1
			longest = max(longest, j - arr[i])
	return longest




T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	ans.append(longest_subsequence(arr))

for a in ans:
	print(a)