#input takes numbers and raw input takes strings 
def pattern(N):
	for i in range(N, 0, -1):
		for j in range(N, 0, -1):
			for z in range(0, i):
				print(j),
		print('$'),

T = input() 
N = []
for i in range(0, T):
	N.append(input())

for i in N:
	pattern(i)
	print("") #or just print
