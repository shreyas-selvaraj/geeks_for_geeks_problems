#the rectangles are parallel to coordinate axes, just check if one is bounded by other 

def isOverlap(coords1, coords2):
	otherCoords1 = [coords1[0], coords1[3], coords1[2], coords1[1]] #bottom left, top right
	for coord in otherCoords1:
		coords1.append(coord)
		
	rightUpperBound = coords2[2]
	rightLowerBound = coords2[0]
	topUpperBound = coords2[1]
	topLowerBound = coords2[3]
	#for any one rectangle, see if one of the coordinates fits with bounds of other rectangle 
	#right bounds is x of right given coord, top bounds is y of left coord

	for i in range(0, len(coords1), 2):
		if(coords1[i] <= rightUpperBound and coords1[i] >= rightLowerBound
			and coords1[i+1] <= topUpperBound and coords1[i+1] >= topLowerBound):
			return True

	return False


T = input()
ans = []

for i in range(T):
	#two lines of input for each T 
	rect1 = [int(x) for x in raw_input().split(" ")]
	rect2 = [int(y) for y in raw_input().split(" ")]
	ans.append(isOverlap(rect1, rect2))

for a in ans:
	print(a)