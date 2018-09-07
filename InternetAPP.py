import time as t

class internet:
	def __init__(self, Alice_t = 1, check_t = 3, bob_t = 7):
		self.Alice_t = Alice_t
		self.check_t = check_t
		self.bob_t = bob_t
		self.Alice = 0
		self.bob = 0

	def Alice_mt(self, Alice_t):
		self.Alice_t = Alice_t

	def check_mt(self, check_t):
		self.check_t = check_t

	def bob_mt(self, bob_t):
		self.bob_t = bob_t

	def make_p(self):
		self.Alice += 1

	def check_A(self):
		self.bob += self.Alice
		self.Alice = 0

	def check_B(self):
		self.bob = 0

	def start(self, fin = 20):
		time = 1
		while 1:
			try:
				if time == fin:
					break
				if time % self.Alice_t == 0:
					self.make_p()
				if time % self.check_t == 0:
					self.check_A()
				if time % self.bob_t == 0:
					self.check_B()
				print([time, self.Alice, self.bob])
				time += 1
				t.sleep(1)
			except:
				break

a = internet()
a.start()