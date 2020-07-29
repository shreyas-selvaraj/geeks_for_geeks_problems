def isPalindrome(string):
	s = 0
	end = len(string) - 1
	while(s < end):
		if(string[s] != string[end]):
			return "No"
		s += 1
		end -= 1
	return "Yes"

T = int(input())
ans = []

for i in range(T):
	N = input()
	string = input()
	ans.append(isPalindrome(string))

for a in ans:
	print(a)