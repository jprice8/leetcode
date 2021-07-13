

class Solution:
	def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

		first = ""
		for i in firstWord:
			first += str(ord(i) - 97)

		second = ""
		for i in secondWord:
			second += str(ord(i) - 97)

		target = ""
		for i in targetWord:
			target += str(ord(i) - 97)

		if int(first) + int(second) == int(target):
			return True
		else:
			return False 


s = Solution()
print(s.isSumEqual('j', 'j', 'bi'))
