def is_power(x, y):
	curr = x
	if(x == 0):
		return False
	if(x == 1 and y != 1):
		return False
	while(curr <= y):
		if(curr == y):
			return True
		else:
			curr *= x
	return False

T = input()
ans = []

for i in range(T):
	inputs = raw_input().split(" ")
	ans.append(is_power(int(inputs[0]), int(inputs[1])))

for a in ans:
	print(a)