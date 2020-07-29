def product_array(arr):
	#array elements are product of all elements besides current element
	#find total prod then replace with total prod/current element
	total_prod = arr[0]
	for i in range(1, len(arr)):
		total_prod *= arr[i]

	for j in range(0, len(arr)):
		arr[j] = total_prod // arr[j]

	return arr

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	ans.append(product_array(arr))

for a in ans:
	print(a)