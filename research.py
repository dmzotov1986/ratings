import ratings, random
def draw(n):
	n += n & 1
	tour = ((p, n + 1 - p) for p in range(1, n // 2 + 1))
	substitution = Substitution(n)
	while True:
		yield tour
		#Проверять n
		if tour[0][1] == 2:
			return
		tour = (substitution.match(*match) for match in tour)
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
	#есть оптимальнее ветвление?
	if not random.getrandbits(4):
		result = 2 - result
	print(result, end = " ")
	return result
n = int(input("Количество участников: "))
t = int(input("Количество круговых турниров: "))
rank_to_rating = [ratings.INITIAL_RATING for _ in range(n + 1)]#по другому
#чаще смотрится рейтинг, чем настоящее место?
place_to_rank = [rank for rank in range(n + 1)]#по другому и от 0 все
for _ in range(t):
	place_to_rank1 = place_to_rank[1:]
	random.shuffle(place_to_rank1)
	place_to_rank[1:] = place_to_rank1
	for tour in draw(n):
		for match in tour:
			p1, p2 = (place_to_rank[p] for p in match)
			rank_to_rating[p1], rank_to_rating[p2] = ratings.update(rank_to_rating[p1], rank_to_rating[p2], result(p1, p2))
		print()
		for rating in rank_to_rating[1:]:
			print(rating, end = " ")
		print()