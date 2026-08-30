import ratings, random
def draw(n):
	n += n & 1
	tour = tuple((p, n + 1 - p) for p in range(1, n // 2 + 1))
	substitution = Substitution(n)
	while True:
		yield tour
		if tour[0][1] == 2:
			return
		tour = tuple(substitution.match(*match) for match in tour)
class Substitution:#на глобальную переменную?
	def __init__(self, n):
		self._n = n
	def player(self, p):
		if p > 2:
			return p - 1
		if p == 2:
			return self._n
		return 1
	def match(self, p1, p2):
		if p1 == 1 or p2 == 1:
			p1, p2 = p2, p1
		return self.player(p1), self.player(p2)
def result(p1, p2):
	#Последний игрок иногда отсутствует!
	#Другая жеребьёвка, другие рейтинги (для ручных сортировок).
	print((p1, p2), end = ":")
	if abs(p1 - p2) <= 2 and random.choice((False, True)):
		result = 1
	elif p1 < p2:
		result = 2
	else:
		result = 0
	print(result, end = " ")
	return result
n = int(input("Количество участников: "))
t = int(input("Количество круговых турниров: "))
player_ratings = [ratings.INITIAL_RATING for _ in range(n + 1)]
place_to_rank = [rank for rank in range(1, n + 1)]
ptr = [0]
for _ in range(t):
	random.shuffle(place_to_rank)
	ptr[1:] = place_to_rank
	for tour in draw(n):
		for match in tour:
			p = tuple(ptr[p] for p in match)
			player_ratings[p[0]], player_ratings[p[1]] = ratings.update(player_ratings[p[0]], player_ratings[p[1]], result(p[0], p[1]))
		print()
		for rating in player_ratings[1:]:
			print(rating, end = " ")
		print()