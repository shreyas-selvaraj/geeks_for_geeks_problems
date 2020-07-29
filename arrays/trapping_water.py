def calculate_water(sindex, eindex, region_height, arr):
	amt = 0
	for i in range(sindex, eindex + 1):
		if(region_height - arr[i]) > 0:
			amt += region_height - arr[i]
	return amt

def trapping_water(arr):
	#water left is total height - height of blocks for each index 
	#total height is min of two block heights 
	#edge case is where there is small block in the middle of two big blocks 
	#need to keep track of 0s too

	#go through once keep track of block positions, for each block until u hit a bigger block add to total amount
	#once u hit bigger block set new min and do the same 
	#once u hit a bigger block u can go back and set the total height for the region
	#then substract from total height

	sblock = 0
	e_block = 0
	amt = 0
	blocks = [] #index of only blocks

	for i in range(len(arr)):
		if(arr[i] > 0):
			blocks.append(i)

	j = 0
	while(j < len(blocks) - 1):
		for k in range(j + 1, len(blocks)):
			if(arr[blocks[k]] >= arr[blocks[j]]):
				amt += calculate_water(blocks[j], blocks[k], min(arr[blocks[k]], arr[blocks[j]]), arr)
				j = k - 1 #setting new minimum, but gets incremented at end 
				break
		j += 1
	return amt

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	ans.append(trapping_water(arr))

for a in ans:
	print(a)

#FOR I IN RANGE AUTOMATICALLY MAKES I EVERY VALUE NEED WHILE TO SKIP VALUES