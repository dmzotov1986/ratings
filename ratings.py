class Rating:
	def __init__(self, rating = 0.0):
		self.rating = rating
	def update(self, other, result):
	#result от 0 до 2 для первого игрока
		increase = result - 2 / (10 ** ((other.rating - self.rating) / 25) + 1)
		self.rating += increase
		other.rating -= increase