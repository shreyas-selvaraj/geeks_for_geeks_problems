def chocolate_dist(arr, students):
	#each packet has dif amount
	#packets need to be distributed to students 
	#each students gets one packet
	#dif between number chocolates given to student with max packet and student with min packet
	#is a minimum
	#problem doesnt make sense?

T = input()
ans = []

for i in range(T):
	N = input()
	arr = [int(x) for x in raw_input().split(" ")]
	students = input()
	ans.append(chocolate_dist(arr, students))

for a in ans:
	print(a)