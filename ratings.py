from operator import *
INITIAL_RATING = 0.0
def update(match, result):
	if not 0 <= result <= 2:
		raise ValueError("Результат матча для первого игрока от 0 до 2")
	match = tuple(match)
	increase = result - 2 / (10 ** ((sub(*reversed(match))) / 25) + 1)
	#increase?
	return map(add, match, (increase, -increase))