import ratings, random
class Draw:
	def __init__(self, n):
		#Нечетные неправильно работают, нужен ещё тур! Надёжнее лишний игрок, с которым отдыхают. Только для исследований, некоторые дефекты.
		self.n = n
		self.tour = tuple((p, n + 1 - p) for p in range(1, (n + 1) // 2 + 1))
	def next(self):
		self.tour = tuple((self.substitute(p1), self.substitute(p2)) for p1, p2 in self.tour)
	def substitute(self, p):
		p -= 1
		if p > 1:
			return p
		if p:
			return self.n
		return 1
def result(p1, p2):
	#Другая зависимость, другая жеребьёвка, другие рейтинги (для ручных сортировок).
#	if p1 < p2:
#		return 2
#	elif p1 == p2:
#		return 1
#	else:
#		return 0
	if abs(p1 - p2) <= 2:
		if random.choice((False, True)):
			return 1
	if p1 < p2:
		return 2
	return 0
n = int(input("N?: "))
t = int(input("T?: "))
draw = Draw(n)
ratings = [ratings.Rating() for _ in range(n + 1)]
for _ in range((n - 1) * t):
	print(draw.tour)
	for p1, p2 in draw.tour:
		ratings[p1].update(ratings[p2], result(p1, p2))
	for rating in ratings[1:]:
		print(rating.rating, end = " ")
	print()
	draw.next()