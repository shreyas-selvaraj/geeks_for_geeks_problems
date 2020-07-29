def nthevenfib(N):
	#odd + odd = even 
	#odd + even = odd
	#even + even = even
	#1,1,2,3,5,8,13,21...
	#instead of going through sequence and counting evens
	#find position of number then print num, same time complexity tho
	p1 = 1
	p2 = 1
	s = 0
	counter = 0

	while(counter != N):
		s = p1 + p2
		if(s % 2 == 0):
			counter += 1
		p1 = p2
		p2 = s
	return s 

T = input()
ans = []

for i in range(T):
	ans.append(nthevenfib(input()))

for a in ans:
	print(a)