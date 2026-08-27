import ratings, random
def draw(n):
	#Нечетные неправильно работают, нужен ещё тур! Надёжнее лишний игрок, с которым отдыхают.
	n += n & 1
	tour = tuple((p, n + 1 - p) for p in range(1, n // 2 + 1))
	while True:
		yield tour
		if tour[0][1] == 2:
			return
		tour = tuple(substitute_match(*match, n) for match in tour)
def substitute(p, n):#перевести на объект?
	if p > 2:
		return p - 1
	if p == 2:
		return n
	return 1
def substitute_match(p1, p2, n):
	if p1 == 1 or p2 == 1:
		p1, p2 = p2, p1
	return substitute(p1, n), substitute(p2, n)
def result(p1, p2):
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
#Нужна подстановка место/сила!
ratings = [ratings.Rating() for _ in range(n + 1)]
for _ in range(t):
	for tour in draw(n):
		for p1, p2 in tour:
			ratings[p1].update(ratings[p2], result(p1, p2))
		print()
		for rating in ratings[1:]:
			print(rating.rating, end = " ")
		print()