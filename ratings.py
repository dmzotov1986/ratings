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
class Draw:
	def __init__(self, n):
		self._n = n
draw = Draw(5)
variants = [i for i in range(1, int(input("N?: ")) + 1)]
used = set()
tour = []
calls = 0
def next_match(match, variants, used, tour):
	global calls
	if match:
		used.add(match)
		tour.append(match)
		variants.remove(match[1])
	if variants:
		p1 = variants.pop(0)
		for p2 in variants:
			match = (p1, p2)
			if p1 == 1:
				print("Match:", match)
			if match in used:
				continue
			calls = calls + 1
			if calls == 500000:
				print("Tour:", tour)
				calls = 0
			if data := next_match(match, variants.copy(), used.copy(), tour.copy()):
				if p1 == 1:
					print(data[1])
					used = data[0]
					continue
				return data
		return False
	return used, tour
next_match(None, variants, used, tour)
#1:2 3:4 5:6
#1:3 2:5 4:6
#1:4 2:6 3:5
#1:5 2:4 3:6
#1:6 2:3 4:5