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
n = 6
c = (n + 1) // 2
t = [[None] * (c + 1) for _ in range(n)]
for p1 in range(1, n + 1):
	for p2 in range(p1 + 1, n + 1):
		for i in range(1, n):
			for j in range(1, c + 1):
				if t[i][j] == None:
					for k in range(1, j):
						if t[i][k][1] == p1 or t[i][k][1] == p2 or t[i][k][2] == p1 or t[i][k][2] == p2:
							break
					else:
						t[i][j] = [None, p1, p2]
						break_i = True
						break
					break_i = False
					break
			if break_i:
				break
for i in range(1, n):
	for j in range(1, c + 1):
		print(f"{t[i][j][1]:2}:{t[i][j][2]:2}", end = " ")
	print()
#1:2 3:4 5:6
#1:3 2:5 4:6
#1:4 2:6 3:5
#1:5 2:4 3:6
#1:6 2:3 4:5