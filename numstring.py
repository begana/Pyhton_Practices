class Numstring:
	def __init__(self, value):
		self.value = str(value)

	def __str__(self):
		return str(self.value)

	def __int__(self):
		return int(self.value)

	def __float__(self):
		return float(self.value)