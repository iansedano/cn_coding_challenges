def find_floor(directions: str):
	floor = 0
	for dir in directions:
		if dir == "(":
			floor += 1
		elif dir == ")":
			floor -= 1
	return floor

# Another solution
def find_floor2(directions:str):
	return sum(map(lambda d: 1 if d == "(" else -1, directions))
