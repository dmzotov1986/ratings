for module in ("random", "ratings", "itertools", "operator"):
	exec(f"from {module} import *")
#map как add???
def table_of_matches(n):
	if n & 1:
		raise ValueError("Количество участников чётное")
	tour = tuple(takewhile(lambda match: lt(*match), zip(count(1), count(n, -1))))
	def substitute_player(p):
		match p:
			case _ if p > 2:
				return p - 1
			case 2:
				return n
			case _:
				return 1
	def substitute_match(match):
		if 1 in match:
			match = reversed(match)
		return tuple(map(substitute_player, match))
	def supply_tour():
		nonlocal tour
		while True:
			yield tour
			tour = tuple(map(substitute_match, tour))
	return islice(supply_tour(), n - 1)
def result(match):
	#Другая жеребьёвка, другие рейтинги. Для ручных сортировок.
	print(match, end = ":")
	distance = abs(sub(*match))
	match distance:
		case 0 | _ if random() < 1 / (distance ** (1 / 3) + 1):
			result = 1
		case _ if lt(*match):
			result = 2
		case _:
			result = 0
	if random() < 1 / (distance + 15):
		result = 2 - result
	print(result, end = " ")
	return result
n = int(input("Количество участников: "))
rank_to_rating = dict.fromkeys(islice(count(1), n), INITIAL_RATING)
odd = n & 1
n += odd
t = int(input("Количество круговых турниров: "))
place_to_rank = dict(enumerate(islice(count(1), n), 1))
#Круговая система, очки для сравнения
for _ in range(t):
	ranks = list(place_to_rank.values())
	shuffle(ranks)
	place_to_rank = dict(enumerate(ranks, 1))
	for tour in table_of_matches(n):
		for match in tour:
			match = tuple(map(place_to_rank.get, match))
			if not(odd and n in match):
				rank_to_rating.update(zip(match, update(map(rank_to_rating.get, match), result(match))))
		print()
		print(sorted(rank_to_rating.items(), key=itemgetter(1), reverse=True))