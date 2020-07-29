def isTriangular(N):
	counter = 0 
	i = 1
	while(counter < N):
		counter += i
		i += 1

	if(counter == N):
		return 1
	else:
		return 0

T = input()
ans = []

for i in range(T):
	ans.append(isTriangular(input()))

for a in ans:
	print(a)