class Rating:
	def __init__(self, rating = 0.0):
		self.rating = rating
	def won(self, other):
		self.update(other, 2)
	def draw(self, other):
		self.update(other, 1)
	def lost(self, other):
		self.update(other, 0)
	def update(self, other, result):
		increase = result - 2 / (10 ** ((other.rating - self.rating) / 25) + 1)
		self.rating += increase
		other.rating -= increase
class Draw:
	def __init__(self, n):
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
n = int(input("N?: "))
draw = Draw(n)
print(draw.tour)
for _ in range(n - 2):
	draw.next()
	print(draw.tour)