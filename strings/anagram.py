#add characters for first into hashtable
#go through second string, then either delete from second string or decrement hashtable

def isAnagram(str1, str2):
	d = {}
	for char in str1:
		if char in d.keys():
			d[char] += 1
		else:
			d[char] = 1
	for char in str2:
		if char in d.keys():
			d[char] -= 1
		else:
			return "NO"
	for key in d.keys():
		if(d[key] != 0):
			return "NO"
	return "YES"

T = int(input())
ans = []

for i in range(T):
	strings = input().split(" ")
	ans.append(isAnagram(strings[0], strings[1]))

for a in ans:
	print(a)