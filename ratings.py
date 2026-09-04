INITIAL_RATING = 0.0
def update(first, second, result):
	if not 0 <= result <= 2:
		raise ValueError("Результат матча для первого игрока от 0 до 2")
	increase = result - 2 / (10 ** ((second - first) / 25) + 1)
	first += increase
	second -= increase
	return first, second