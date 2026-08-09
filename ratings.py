class Rating:
	def __init__(self, rating = 0.0):
		self._rating = rating
	@property
	def rating(self):
		return self._rating
	def update(self, other, result):
		if result < 0 or result > 2:
			raise ValueError("Результат от 0 до 2")
		increase = result - 2 / (10 ** ((other.rating - self.rating) / 25) + 1)
		self._rating += increase
		other._rating -= increase
	def won(self, other):
		self.update(other, 2)
	def draw(self, other):
		self.update(other, 1)
	def lost(self, other):
		self.update(other, 0)
inputs = list(map(float, input("Введите рейтинги двух игроков и результат матча (количество набранных очков первым игроком - 0, 1, 2): ").split()))
first, second = ratings = [Rating(i) for i in inputs[:-1]]
first.update(second, inputs[2])
print("Рейтинги игроков:", [r.rating for r in ratings])