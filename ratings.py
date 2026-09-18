for module in ("random", "itertools", "operator"):
	exec(f"from {module} import *")
INITIAL_RATING = 0.0
def update():
	res = result()
	for rank, score in zip(match_r, (res, 2 - res)):
		rank_to_score[rank] += score
	ratings = []
	for rank in match_r:
		ratings.append(rank_to_rating[rank])
	r1, r2 = ratings
	increase = res - 2 / (10 ** ((r2 - r1) / 25) + 1)
	for rank, increase in zip(match_r, (increase, -increase)):
		rank_to_rating[rank] += increase
def table_of_matches():
	#Без генераторов
	tour = []
	for p1, p2 in zip(count(0), count(n, -1)):
		if p1 >= p2:
			break
		tour.append([p1, p2])
	def tour_supplier():
		while True:
			yield tour
			for match in tour:
				if 0 in match:
					match.reverse()
				for i, p in enumerate(match):
					p -= 1
					if p <= 0:
						if p == 0:
							p = n
						else:
							p = 0
					match[i] = p
	return islice(tour_supplier(), n)
def result():
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
	return result
n = int(input("Количество участников: "))
rank_to_rating = [INITIAL_RATING] * n
rank_to_score = [0] * n
odd = n & 1
n += odd
place_to_rank = list(range(n))
n -= 1
t = int(input("Количество круговых турниров: "))
for _ in range(t):
	shuffle(place_to_rank)
	for tour in table_of_matches():
		for match in tour:
			match_r = []
			for p in match:
				match_r.append(place_to_rank[p])
			if not(odd and n in match_r):
				update()
		print()
		print(rank_to_rating)
		print(rank_to_score)