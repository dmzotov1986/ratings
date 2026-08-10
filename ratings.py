class Rating:
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
	def __init__(self, rating = 0.0):
		self._rating = rating
inputs = list(map(float, input("Введите рейтинги двух игроков и результат матча (количество набранных очков первым игроком - 0, 1, 2): ").split()))
first, second = ratings = [Rating(i) for i in inputs[:-1]]
first.update(second, inputs[2])
print("Рейтинги игроков:", " ".join([str(r.rating) for r in ratings]))