def findNth(a, b, N):

	d = b - a
	ans.append(a + (N-1) * d)

T = input()
ans = []

for i in range(T):
	vals = raw_input().split(" ")
	N = input()
	findNth(int(vals[0]), int(vals[1]), N)

for i in ans:
	print(i)