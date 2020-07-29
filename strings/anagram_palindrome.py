def anagram_palindrome(string):
	d = {}
	n = len(string)
	counter = 0

	for char in string:
		if char in d.keys():
			d[char] += 1
		else:
			d[char] = 1

	for key in d.keys():
		if(d[key] % 2 == 1):
			counter += 1

	if(n % 2 == 0):
		if counter == 0:
			return "Yes"
		else:
			return "No"

	else:
		if counter == 1:
			return "Yes"
		else:
			return "No"


T = int(input())
ans = []

for i in range(T):
	ans.append(anagram_palindrome(input()))

for a in ans:
	print(a)