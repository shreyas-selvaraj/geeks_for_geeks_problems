def buy_and_sell(arr):
	bounds = []
	si = 0
	ei = 0
	curr_price = arr[0]

	for i in range(1, len(arr)):

		if(i == len(arr) - 1 and arr[i] > curr_price):
				ei = i
				bounds.append((si, ei))


		elif(arr[i] < curr_price):
			ei = i - 1
			if(abs(ei-si) > 0):
				bounds.append((si, ei))
			si = i
		curr_price = arr[i]
	return bounds

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	ans.append(buy_and_sell(arr))

for a in ans:
	print(a)