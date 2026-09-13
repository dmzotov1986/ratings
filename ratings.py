INITIAL_RATING = 0.0
def update(match, result):
	if not 0 <= result <= 2:
		raise ValueError("Результат матча для первого игрока от 0 до 2")
	p1, p2 = match
	increase = result - 2 / (10 ** ((p2 - p1) / 25) + 1)
	p1 += increase
	p2 -= increase
	return p1, p2