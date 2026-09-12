from random import shuffle, random
from ratings import *
from itertools import islice, count
from operator import itemgetter
def table_of_matches(n):
	if n & 1:
		raise ValueError("Количество участников чётное")
	#map
	#takewhile
	tour = tuple((p1, p2) for p1, p2 in zip(count(1), count(n, -1)) if p1 < p2)
	k = n
	def substitute_player(p):
		if p > 2:
			return p - 1
		if p == 2:
			return n
		return 1
	def substitute_match(match):
		if any(p == 1 for p in match):
			match = reversed(match)
		p1, p2 = match
		return substitute_player(p1), substitute_player(p2)
	while True:
		yield tour
		if k <= 2:
			return
		k -= 1
		tour = tuple(map(substitute_match, tour))
def result(p1, p2):
	#Другая жеребьёвка, другие рейтинги. Для ручных сортировок.
	print((p1, p2), end = ":")
	if random() < 1 / (abs(p1 - p2) ** (1 / 3) + 1):
		result = 1
	elif p1 < p2:
		result = 2
	else:
		result = 0
	if random() < 1 / (abs(p1 - p2) + 15):
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
			match = tuple(map(place_to_rank.__getitem__, match))
			#filter?
			if not(odd and any(p == n for p in match)):
				p1, p2 = match
				rank_to_rating[p1], rank_to_rating[p2] = update(rank_to_rating[p1], rank_to_rating[p2], result(p1, p2))
		print()
		print(sorted(rank_to_rating.items(), key=itemgetter(1), reverse=True))