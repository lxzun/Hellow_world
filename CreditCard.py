class CreditCard:
	def __init__(self, customer, bank, acnt, limit, balance=0):
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = balance

	def get_cus(self):
		return self._customer

	def get_bank(self):
		return self._bank
	
	def get_acnt(self):
		return self._account
	
	def get_limit(self):
		return self._limit
	
	def get_bal(self):
		return self._balance
	
	def charge(self, price):
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self, amount):
		self._balance -= amount