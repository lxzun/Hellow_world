class Vector:
	def __init__(self, d):
		self._coords = [0] * d

	def __len__(self):
		return len(self._coords)

	def __getitem__(self, j):
		return self._coords[j]

	def __setitem__(self, j, val):
		self._coords[j] = val
	
	def __mul__(self, other):
		if type(other) == Vector:
			if len(self) != len(other):
				raise ValueError('dimensions must agree')

			result = 0
			for i in range(len(self)):
				result += self[i] * other[i]
			return result


		else:
			result = Vector(len(self))
			for j in range(len(self)):
				result[j] = self[j]*other
			return result

	def __add__(self, other):
		if len(self) != len(other):
			raise ValueError('dimensions must agree')

		result = Vector(len(self))
		
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		
		return result

	def __eq__(self, other):
		return self._coords == other._coords

	def __ne__(self, other):
		return not self == other

	def __str__(self):
		return '<' + str(self._coords)[1:-1] + '>'

a = Vector(5)
b = Vector(5)

for i in range(5):
	a[i] = i
	b[i] = 5-i

print(a,b,a*3,a*b)
