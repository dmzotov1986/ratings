import ratings, random, operator
def table_of_matches(n):
	if n & 1:
		raise ValueError("Количество участников чётное")
	tour = tuple((p, n + 1 - p) for p in range(1, n // 2 + 1))
	k = n
	def substitute_player(p):
		if p > 2:
			return p - 1
		if p == 2:
			return n
		return 1
	def substitute_match(match):
		p1, p2 = match
		if not p1 != 1 != p2:
			p1, p2 = p2, p1
		return substitute_player(p1), substitute_player(p2)
	while True:
		yield tour
		if k <= 2:
			return
		k -= 1
		tour = tuple(substitute_match(match) for match in tour)
def result(p1, p2):
	#Другая жеребьёвка, другие рейтинги. Для ручных сортировок.
	print((p1, p2), end = ":")
	if random.random() < 1 / (abs(p1 - p2) ** (1 / 3) + 1):
		result = 1
	elif p1 < p2:
		result = 2
	else:
		result = 0
	if random.random() < 1 / (abs(p1 - p2) + 15):
		result = 2 - result
	print(result, end = " ")
	return result
n = int(input("Количество участников: "))
rank_to_rating = dict.fromkeys(range(1, n + 1), ratings.INITIAL_RATING)
odd = n & 1
n += odd
t = int(input("Количество круговых турниров: "))
place_to_rank = dict(enumerate(range(1, n + 1), 1))
#0 n или 1 n? Для нечетных
#Круговая система, очки для сравнения
for _ in range(t):
	ranks = list(place_to_rank.values())
	random.shuffle(ranks)
	place_to_rank = dict(enumerate(ranks, 1))
	for tour in table_of_matches(n):
		for match in tour:
			p1, p2 = (place_to_rank[p] for p in match)
			#Вывести отдыхающего тоже.
			if not odd or p1 != n != p2:
				rank_to_rating[p1], rank_to_rating[p2] = ratings.update(rank_to_rating[p1], rank_to_rating[p2], result(p1, p2))
		print()
		print(sorted(rank_to_rating.items(), key=operator.itemgetter(1), reverse=True))