for module in ("random", "itertools", "operator"):
	exec(f"from {module} import *")
INITIAL_RATING = 0.0
def table_of_matches():
	#Без генераторов
	tour = [None] * m
	for i in range(m):
		tour[i] = [None, None]
	for i, p1, p2 in zip(range(m), count(0), count(n, -1)):
		p = p2
		for j in count(1, -1):
			tour[i][j] = p
			if not j:
				break
			p = p1
	def tour_supplier():
		while True:
			yield tour
			for i in range(m):
				match = tour[i]
				if 0 in match:
					match.reverse()
				for j in range(2):
					p = match[j]
					p -= 1
					if p <= 0:
						if p == 0:
							p = n
						else:
							p = 0
					match[j] = p
	return islice(tour_supplier(), n)
n = int(input("Количество участников: "))
rank_to_rating = [INITIAL_RATING] * n
rank_to_score = [0] * n
odd = n & 1
n += odd
place_to_rank = [None] * n
for i in range(n):
	place_to_rank[i] = i
m = n // 2
n -= 1
t = int(input("Количество круговых турниров: "))
for _ in range(t):
	shuffle(place_to_rank)
	for tour in table_of_matches():
		for match in tour:
			match_r = [None] * 2
			for i, p in enumerate(match):
				match_r[i] = place_to_rank[p]
			if not(odd and n in match_r):
				#Другая жеребьёвка, другие рейтинги, для ручных сортировок.
				print(match_r, end = ":")
				p1, p2 = match_r
				distance = abs(p1 - p2)
				match distance:
					case 0 | _ if random() < 1 / (distance ** (1 / 3) + 1):
						result = 1
					case _ if p1 < p2:
						result = 2
					case _:
						result = 0
				if random() < 1 / (distance + 15):
					result = 2 - result
				print(result, end = " ")
				for rank, score in zip(match_r, (result, 2 - result)):
					rank_to_score[rank] += score
				ratings = []
				for rank in match_r:
					ratings.append(rank_to_rating[rank])
				r1, r2 = ratings
				increase = result - 2 / (10 ** ((r2 - r1) / 25) + 1)
				for rank, increase in zip(match_r, (increase, -increase)):
					rank_to_rating[rank] += increase
		print()
		print(rank_to_rating)
		print(rank_to_score)