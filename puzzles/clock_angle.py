#assign each minute and hour an angle, find dif in angles, need to return two angles 
import math

def angle(h, m):
	hangle = 360/12 * (h + m/60.0) #hour hand moves, doesn't stay at number 
	if hangle > 360:
		hangle = hangle - 360
	mangle = 360/60 * m
	dif1 = math.floor(max(hangle, mangle) - min(hangle,mangle))
	dif2 = 360 - dif1
	return dif1, dif2
	#implement way to find between hands in clockwise direction so that it's actually between not on either side 

T = input()
ans = []

for i in range(T):
	inputs = [int(x) for x in raw_input().split(" ")]
	ans.append(angle(inputs[0], inputs[1]))

for a in ans:
	print(a[0]),
	print(a[1])