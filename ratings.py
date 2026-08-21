class Rating:
	def __init__(self, rating = 0.0):
		self.rating = rating
	def update(self, other, result):
		increase = result - 2 / (10 ** ((other.rating - self.rating) / 25) + 1)
		self.rating += increase
		other.rating -= increase
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
	if p1 < p2:
		return 2
	elif p1 == p2:
		return 1
	else:
		return 0
n = int(input("N?: "))
draw = Draw(n)
#for _ in range(n - 1):
#	print(draw.tour)
#	draw.next()
ratings = [Rating() for _ in range(n + 1)]
for _ in range((n - 1) * 1000):
	for p1, p2 in draw.tour:
		ratings[p1].update(ratings[p2], result(p1, p2))
	print(" ".join(str(r.rating) for r in ratings[1:]))
	draw.next()
#Исследование в отдельном файле.