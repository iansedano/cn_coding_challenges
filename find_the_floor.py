def find_floor(directions: str):
	floor = 0
	for dir in directions:
		if dir == "(":
			floor += 1
		elif dir == ")":
			floor -= 1
	return floor
