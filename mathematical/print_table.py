def print_table(N):
	for i in range(1, 11):
		print(N * i),

T = input()
N = []
for i in range(T):
	N.append(input())

for j in N:
	print_table(j)
	print
