class Rating:
	def __init__(self, rating = 0.0):
		self._rating = rating
	@property
	def rating(self):
		return self._rating
	def update(self, other, result):
		if result < 0 or result > 2:
			raise ValueError("Результат матча для первого игрока от 0 до 2")
		increase = result - 2 / (10 ** ((other._rating - self._rating) / 25) + 1)
		self._rating += increase
		other._rating -= increase