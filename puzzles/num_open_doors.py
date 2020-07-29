import math

def count_factors(N):
	#count numbers up to sqrt, then double 
	counter = 0
	if( N == 1):
		return 1
	for i in range(2, int(math.sqrt(N))):
		if N % i == 0:
			counter += 1

	counter *= 2 #get multiples on other side of root
	if(math.sqrt(N) == math.floor(math.sqrt(N))):
		counter = counter + 1


	return counter

def num_open_doors(N):
	#for every number their state is dependent on how many factors they have 
	#all doors closed initially
	counter = 1
	for i in range(2, N + 1):
		if count_factors(i) % 2  == 1:
			counter += 1
	return counter

#BETTER VERSION, LOOK AT COMPLEXITY 
def num_open_doors_2(N):
	#for every number their state is dependent on how many factors they have 
	#all doors closed initially
	#off by one for squares, look at above how that plays into it 
	p = 1
	counter = 0
	arr = [False for i in range(N)]
	for i in range(1, N+1):
		while((p * i) <= N - 1):
			arr[p * i] = not(arr[p * i])
			p += 1
		p = 1
	for a in arr:
		if a == True:
			counter = counter + 1
	return counter

T = input()
ans = []

for i in range(T):
	ans.append(num_open_doors(input()))

for a in ans:
	print(a)

#start with opposite of starting because going through first time, guarantees everything switched