import ratings, random
class Draw:
	def __init__(self, n):
		#Нечетные неправильно работают, нужен ещё тур! Надёжнее лишний игрок, с которым отдыхают. Только для исследований, некоторые дефекты.
		self.n = n
		self.tour = tuple((p, n + 1 - p) for p in range(1, (n + 1) // 2 + 1))
	def next(self):
		def substitute(p):
			p -= 1
			if p > 1:
				return p
			if p:
				return self.n
			return 1
		self.tour = tuple((substitute(p1), substitute(p2)) for p1, p2 in self.tour)
def result(p1, p2):
	print((p1, p2), end = ":")
	#Другая жеребьёвка, другие рейтинги (для ручных сортировок).
	if abs(p1 - p2) <= 2:#одно условие и abs заменить
		if random.choice((False, True)):
			print(1, end = " ")
			return 1
	if p1 < p2:
		print(2, end = " ")
		return 2
	print(0, end = " ")
	return 0
n = int(input("N?: "))
t = int(input("T?: "))
draw = Draw(n)
ratings = [ratings.Rating() for _ in range(n + 1)]
for _ in range(t):
	for _ in range(n - 1):
		for p1, p2 in draw.tour:
			ratings[p1].update(ratings[p2], result(p1, p2))
		print()
		for rating in ratings[1:]:
			print(rating.rating, end = " ")
		print()
		draw.next()