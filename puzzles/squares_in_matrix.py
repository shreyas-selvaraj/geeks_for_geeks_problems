def move(dim, er, ec, r, c):
	#er and ec are ending coordinates, shift ec and er by one every time for given square size 
	counter = 0
	temp = ec
	while er <= r:
		while ec <= c:
			counter += 1
			ec += 1
		ec = temp
		er += 1
	return counter

def num_squares(sr, sc, r, c):
	#create a default square of certain size, then move that to every point within matrix
	num_squares = 0

	for i in range(1, min(r,c) + 1):
		#initializing different squares
		dim = i
		er = dim
		ec = dim
		num_squares += move(dim, er, ec, r, c)
		#move the squares and check
	return num_squares

T = input()
ans = []

for i in range(T):
	inputs = [int(x) for x in raw_input().split(" ")]
	ans.append(num_squares(0, 0, inputs[0], inputs[1]))

for a in ans:
	print(a)

#fix brute force, then find formula 