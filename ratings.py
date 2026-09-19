for module in ("random", "itertools", "operator"):
	exec(f"from {module} import *")
INITIAL_RATING = 0.0
def table_of_matches():
	#Без генераторов
	tour = [None] * m
	for i in range(m):
		tour[i] = [None, None]
	for i, p1, p2 in zip(range(m), count(0), count(n, -1)):
		match_places = tour[i]
		p = p2
		for j in count(1, -1):
			match_places[j] = p
			if not j:
				break
			p = p1
	def tour_supplier():
		while True:
			yield tour
			for i in range(m):
				match_places = tour[i]
				for i in range(2):
					if not match_places[i]:
						match_places[i] = match_places[1 - i]
						match_places[1 - i] = 0
						break
				for j in range(2):
					p = match_places[j]
					p -= 1
					if p <= 0:
						if p == 0:
							p = n
						else:
							p = 0
					match_places[j] = p
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
#Линейное хранение тура?
t = int(input("Количество круговых турниров: "))
for _ in range(t):
	shuffle(place_to_rank)
	for tour in table_of_matches():
		i = 0
		while True:
			match_places = tour[i]
			match_ranks = [None] * 2
			for j in range(2):
				match_ranks[j] = place_to_rank[match_places[j]]
			if odd:
				for j in range(2):
					if match_ranks[j] == n:
						update = False
						break
				else:
					update = True
			else:
				update = True
			if update:
				#Другая жеребьёвка, другие рейтинги, для ручных сортировок.
				for j in count(0):
					print(match_ranks[j], end = "")
					if j == 1:
						break
					print(end = "-")
				for j in range(2):
					exec(f"p{j + 1} = match_ranks[j]")
				diff = p1 - p2
				distance = abs(diff)
				if random() < 1 / (distance ** (1 / 3) + 1):
					result = 1
				elif diff < 0:
					result = 2
				else:
					result = 0
				if random() < 1 / (distance + 15):
					result = 2 - result
				print(" :", result, end = "")
				for rank, score in zip(match_ranks, (result, 2 - result)):
					rank_to_score[rank] += score
				ratings = []
				for rank in match_ranks:
					ratings.append(rank_to_rating[rank])
				r1, r2 = ratings
				increase = result - 2 / (10 ** ((r2 - r1) / 25) + 1)
				for rank, increase in zip(match_ranks, (increase, -increase)):
					rank_to_rating[rank] += increase
			i += 1
			if i >= m:
				break
			print(end = " ")
		print()
		print(rank_to_rating)
		print(rank_to_score)