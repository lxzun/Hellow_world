import random as rd
from time import sleep

class ecosystem:
	def __init__(self, bears = 2, fish = 2, river_size = None):
		num = bears + fish
		if river_size == None or river_size < num:
			print("river size is too small!")
			river_size = num
		self.bears = bears
		self.fish = fish
		self.river_size = river_size
		self.make_new_river()

	def make_new_river(self):
		river_size = self.river_size - self.bears - self.fish
		self.river = [None]*river_size
		for _ in range(self.bears):
			self.river.append('B')
		for _ in range(self.fish):
			self.river.append('F')
		rd.shuffle(self.river)
		print(self.river)

	def make(self, animal):
		if self.river.count(None) > 0:
			index = [i for i, _ in enumerate(self.river) if _ == None]
			self.river[rd.choice(index)] = animal

	def act(self):
		acts = [i for i, _ in enumerate(self.river) if _ != None]
		act = self.river.copy()
		for i in acts:
			act[i] = rd.randint(-1,1)
			if act[i] == 0:
				act[i] = None
		return act

	def system(self, i, act):
		animal = self.river[i]
		if act != 0:
			move = i + act
			if move >= 0 and move < self.river_size:
				if self.river[move] == None:
					self.river[move] = self.river[i]
					self.river[i] = None
				elif self.river[move] == animal:
					self.make(animal)
				else:
					if animal == 'B':
						self.river[move] = 'B'
					self.river[i] = None
		
	def strat(self, act_time = 10):
		time = 0
		while time != act_time:
			act = self.act()
			order = [i for i, _ in enumerate(act) if _ != None]
			rd.shuffle(order)
			for i in order:
				self.system(i, act[i])
			time += 1
			sleep(0.5)
			print(self.river)

A = ecosystem(3,10,25)
A.strat(50)