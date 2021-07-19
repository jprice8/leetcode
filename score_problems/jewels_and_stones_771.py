def jewels_and_stones(jewels: str, stones: str) -> int:
	"""
	Given two strings, jewels and stones, check whether each stone is in
	jewels and return the number of matches.
	"""
	matches = 0
	for i in stones:
		if i in jewels:
			matches += 1
		
	return matches


print(jewels_and_stones(jewels="z", stones="ZZ"))
