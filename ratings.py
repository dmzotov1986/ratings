#class Rating:
#	@property
#	def rating(self):
#		return self._rating
#	def update(self, other, result):
#		if result < 0 or result > 2:
#			raise ValueError("Результат от 0 до 2")
#		self._update(other, result)
#	def won(self, other):
#		self._update(other, 2)
#	def draw(self, other):
#		self._update(other, 1)
#	def lost(self, other):
#		self._update(other, 0)
#	def _update(self, other, result):
#		increase = result - 2 / (10 ** ((other._rating - self._rating) / 25) + 1)
#		self._rating += increase
#		other._rating -= increase
#	def __init__(self, rating = 0.0):
#		self._rating = rating
#class Draw:
#	def __init__(self, n):
#		self._n = n
#draw = Draw(5)
#variants = [i for i in range(1, int(input("N?: ")) + 1)]
#used = set()
#tour = []
#calls = 0
#def next_match(match, variants, used, tour):
#	global calls
#	calls += 1
#	if calls == 500000:
#		print("Tour:", tour)
#		calls = 0
#	if match:
#		used.add(match)
#		tour.append(match)
#		variants.remove(match[1])
#	if variants:
#		p1 = variants.pop(0)
#		for p2 in variants:
#			match = (p1, p2)
#			if p1 == 1:
#				print("Match:", match)
#			if match not in used:
#				all_used = next_match(match, variants.copy(), used.copy(), tour.copy())
#				if all_used:
#					if p1 > 1:
#						return all_used
#					used = all_used
#		return False
#	print(tour)
#	return used
#next_match(None, variants, used, tour)
#Кроме Бергера, оттопыренный от текущего край проверять сначала? Способ швейцарской системы?
def substitute(p):
	if p == 1:
		return 1
	if p == 2:
		return n
	return p - 1
n = int(input("N?: "))
t = [[p1, n + 1 - p1] for p1 in range(1, n // 2 + 1)]
table = []
for _ in range(n - 1):
	table.append(t)
	t2 = []
	for p1, p2 in t:
		match = [substitute(p1), substitute(p2)]
		match.sort()
		t2.append(match)
	t2.sort()
	t = t2
table.reverse()
for t in table:
	print(t)
#Арифметические закономерности, можно считать на программируемом или обычном калькуляторе.