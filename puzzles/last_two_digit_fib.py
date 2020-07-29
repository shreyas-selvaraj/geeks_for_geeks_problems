def last_digits(N):
	#only have to add last two columns to get last two digits 
	#if over 99, then set just get first two places of three digit number
	p1 = 1
	p2 = 1
	s = 0

	for i in range(0, N - 2):
		s = p1 + p2
		p1 = p2
		p2 = s

	if(s < 100):
		return s 
	else:
		return s % 100

T = input()
ans = []

for i in range(T):
	ans.append(last_digits(input()))

for a in ans:
	print(a)