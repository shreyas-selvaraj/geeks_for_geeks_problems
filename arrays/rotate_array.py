def rotate(arr, rs):
	for i in range(rs):
		arr.append(arr.pop(0))
	return arr

T = input()
ans = []

for i in range(T):
	rotation_size = int(raw_input().split(" ")[1]) #ignored N but gfg also has length of array
	inputs = raw_input().split(" ")
	ans.append(rotate(inputs, rotation_size))

for a in ans:
	print(a)