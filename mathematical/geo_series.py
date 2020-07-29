def findNth(a, b, N):
	r = b//a
	vals.append(a * pow(r, N-1))

T = input()
vals = []

for i in range(T):
	string = raw_input().split(" ")
	N = input()
	findNth(float(string[0]), float(string[1]), N)

for i in vals:
	print(i)