import math
def e_distance(x1, y1, x2, y2):
	return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

def calculate_angle(x1, y1, x2, y2, x3, y3, x4, y4):
	return np.arctan(e_distance(x2, y2, x3, y3)/e_distance(x4, y4, x1, y1))

def isSquare(coords):
	#have to check is sides lengths are all same and that the points are not colinear
	#check that the points form a complete shape not just above use arctan  
	dist = e_distance(coords[0], coords[1], coords[2], coords[3])
	for i in range(4, len(coords), 4):
		dist2 = e_distance(coords[i], coords[i+1], coords[i+2], coords[i+3])
		if(dist != dist2):
			return False

	#check arctan between opp/adj equals pi/4, instaed of angles 
	#which is messy, see if u can traverse through points from start point to end point, 
	#hitting all other points only once
	angle = math.pi/4

	return True


T = input()
ans = []

for i in range(T):
	inputs = [int(x) for x in raw_input().split(" ")]
	ans.append(isSquare(inputs))

for a in ans:
	print(a)

