class Rating:
	def __init__(self, rating = 0.0):
		self._rating = rating
	@property
	def rating(self):
		return self._rating
	def update(self, other, result):
		if result < 0 or result > 2:
			raise ValueError("Результат от 0 до 2")
		self._update(other, result)
	def won(self, other):
		self._update(other, 2)
	def draw(self, other):
		self._update(other, 1)
	def lost(self, other):
		self._update(other, 0)
	def _update(self, other, result):
		increase = result - 2 / (10 ** ((other._rating - self._rating) / 25) + 1)
		self._rating += increase
		other._rating -= increase
class Draw:
	def __init__(self, n):
		if n <= 0:
			raise ValueError("Количество участников натуральное число")
		self._n = n
		self._tour = tuple((p, n + 1 - p) for p in range(1, (n + 1) // 2 + 1))
	@property
	def tour(self):
		return self._tour
	def next(self):
		self._tour = tuple((self._substitute(p1), self._substitute(p2)) for p1, p2 in self._tour)
	def _substitute(self, p):
		p -= 1
		if p > 1:
			return p
		if p:
			return self._n
		return 1
n = int(input("N?: "))
draw = Draw(n)
print(draw.tour)
for _ in range(n - 2):
	draw.next()
	print(draw.tour)