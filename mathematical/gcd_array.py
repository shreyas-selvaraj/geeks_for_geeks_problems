def divByArray(arr, val):
 	for i in range(len(arr)):
 		if arr[i] % val != 0:
 			return False
 	return True

def gcd_array(arr):
 	minimum = min(arr)
 	maximum = max(arr)

 	for i in range(len(arr)):
 		while(arr[i] > 0):
 			arr[i] = arr[i] - minimum
 		arr[i] = arr[i] + minimum

	for j in range(minimum, 0, -1):
		if divByArray(arr, j):
			ans.append(j)
			break

T = input()
ans = []

for i in range(T):
	arr = raw_input().split(" ")
	for i in range(len(arr)):
		arr[i] = int(arr[i])
	gcd_array(arr)

for a in ans:
	print(a)