#number zeroes is determined by number of 5s and 2s
#count number of fives, because u need a pair of 5 and 2 to make a ten and there will 
#probably always be more fives and then 

def num_fives(N):
	counter = 0
	while(N % 5 == 0):
		counter+=1
		N /= 5
	return counter

def trailing_zeroes(N):
	#could improve by making sure the twos and fives align, or is that not necessary cuz num 5<2
	counter = 0
	for i in range(1, N+1):
		if i % 5 == 0:
			counter += num_fives(i)
	return counter

T = input()
ans = []

for i in range(T):
	ans.append(trailing_zeroes(input()))

for a in ans:
	print(a)