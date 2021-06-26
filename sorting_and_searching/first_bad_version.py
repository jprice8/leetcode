import random 

def isBadVersion(num):
	return random.choice([True, False])

def firstBadVersion(n):
	left = 1
	right = n 
	while left < right:
		mid = left + (right - left) / 2
		if (isBadVersion(mid)):
			right = mid 
		else:
			left = mid + 1
	return left


print(firstBadVersion(n=5))

def fasterBinarySearch(n):
	l = 0
	r = n 

	while (l < r):
		m = (l+r)//2
		if isBadVersion(m):
			r = m
		else:
			l = m + 1
	return r
