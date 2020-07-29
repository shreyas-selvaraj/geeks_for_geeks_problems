def three_way_partition(arr, low, high):
	#keep one pointer for low, one pointer for high 
	#from left keep going until u encounter number greater than high
	#from right go until u encounter number lower than low and swap 
	#continue until left pointer equals low or right pointer equals high
	#
	#do this then handle middle 
	start = 0
	end = len(arr) - 1
	i = 0

	while(i <= end):
		if(arr[i] < low):
			temp = arr[i]
			arr[i] = arr[start]
			arr[start] = temp
			i += 1
			start += 1

		elif(arr[i] > high):
			temp = arr[i]
			arr[i] = arr[end]
			arr[end] = temp
			end -= 1

		else:
			i += 1

	return arr


T = int(input())
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in input().split(" ")]
	vals = [int(x) for x in input().split(" ")]

	ans.append(three_way_partition(arr, vals[0], vals[1]))

for a in ans:
	print(a)