first, second, result = map(float, input("Введите рейтинги двух игроков и результат матча (количество набранных очков первым игроком - 0, 1, 2): ").split())
increase = result - 2 / (10 ** ((second - first) / 25) + 1)
first += increase
second -= increase
print("Рейтинги игроков:", first, second)
class Rating:
	def __init__(self):
		self.rating = 0
	def update(self, other, result):
		increase = result - 2 / (10 ** ((other.rating - self.rating) / 25) + 1)
		self.rating += increase
		other.rating -= increase