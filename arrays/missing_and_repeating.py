def missing_and_repeating(arr):
	d = {}
	missing = 0
	repeating = 0  
	for i in range(1, len(arr) + 1):
		d[i] = 0

	for j in range(len(arr)):
		d[arr[j]] += 1

	for key in d:
		if d[key] == 0:
			missing = key
		if(d[key] > 1):
			repeating = key

	return repeating, missing

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	ans.append(missing_and_repeating(arr))

for a in ans:
	print(a)