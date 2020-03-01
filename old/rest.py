class reser:
	def __init__(self, name, phon, layout_view_op, menu, reser_info, table_info, layout, request_op):
		self.name = name
		self.phon = phon
		self.date, self.table = self.date(layout_view_op, table_info, reser_info, layout)
		self.menu, self.request = self.selet_menu(menu, request_op)

	def date(self, args):
		A = list(args)
		'booking date and table by option and information'
		return date, table

	def select_menu(self, menu, request_op):
		price = 0
		while 1:
			'select the menu or eixt in a'
			menu = []
			menu.append(a)
			price += menu
			if eixt:
				break
		
		if request_op:
			'input request'

		'inform the dedline to cancel'
		'payment and request'
		return menu, request

	def call(self):
		'sns for the reser'

	def cancel(self):
		'cancel the pay'

class seat:
	def __init__(self, num, limit=None, pos=None):
		self.num = num
		self.limit = limit
		self.pos = pos
		self.use = 0

	def used(slef):
		self.use = 1

	def clear(self):
		self.use = 0

class take_out:
	def __init__(self, name, phon, postpack_op, sns_T_op, menu, number):
		self.name = name
		self.phon = phon
		self.sns = sns_T_op
		self.number = number
		self.menu, distant = self.select_menu(menu, postpack_op)

	def select_menu(self, postpack_op):
		'view the self.number'
		price = 0
		while 1:
			'select the menu or eixt in a'
			menu = []
			menu.append(a)
			price += menu
			if eixt:
				break
		'payment and postpack distant'
		return menu, distant

	def call(self):
		if self.sns:
			'sns for the taker'

class wait:
	def __init__(self, name, phon, layout_view_op, menu, number, table_info, layout, request_op, sns_op):
		self.name = name
		self.phon = phon
		self.number = number
		self.sns = 0
		self.Number of people = 0
		self.want_table = None
		'input the order time(착석 전,후 주문)'
		if order_time:
			self.menu, self.request = self.order(layout_view_op, menu, table_info, layout, request_op, sns_op)
		else:
			self.request = self.seat_order(layout_view_op, layout, table_info, sns_op, request_op)

	def order(self):
		'input the Number of people'
		'view the self.number'

		price = 0
		while 1:
			'select the menu or eixt in a'
			menu = []
			menu.append(a)
			price += menu
			if eixt:
				break
		if layout_view_op:
			'view the layout and select table'
			self.want_table = select_table
		if sns_op:
			'want to sns'
			self.sns = sns

		'inform the dedline to cancel'
		'payment and request'
		return menu, request

	def seat_order(self, layout_view_op, layout, table_info, sns_op):
		'view the self.number'
		if layout_view_op:
			'view the layout and select table'
			self.want_table = select_table
		if sns_op:
			'want to sns'
			self.sns = sns
		if request_op:
			'input request'

		return request


	def call(self):
		if self.sns:
			'sns for the taker'
		
	def cancel(self):
		'cancel the pay'

class menu:
	def __init__(self):
		'input the info of menu'
		self.image = info
		self.name = info
		self.price = info
		self.stock = info

	def mod(self):
		'input mod data'
		self.image = mod_data
		self.name = mod_data
		self.price = mod_data
		self.stock = mod_data

	def __add__(self, other):
		return self.price + other.price

	def __getitem__(self):
		return self.name

class system:
	def __init__(self):
		self.PW = self.PW_set()
		self.view = self.time_set()
		self.reservation_op = self.reser_set()
		self.take_op, self.postpack_op, self.sns_T_op = self.take_set()
		self.table_view_op, self.layout_view_op, self.layout = self.view_set()
		self.request_op, self.sns_op = self.input_set()
		self.menu = []
		self.table = []
		self.take = []
		self.reservation = []
		self.Queue = []
		self.menu_set()
		self.start()

	def PW_set(self):
		'input the PW information in PW'
		return PW

	def time_set(self):
		'input the Restaurant hours and break time and so on for view'
		return [Restaurant_hours, break_time, and_so_on]

	def reser_set(self):
		'input the reservation_op in reservation_op by 0 or 1'
		return reservation_op

	def take_set(self):
		'input take_op by 0 or 1 and if take_op is 1 input the postpack_op and sns_T_op'
		'if take_op is 0, postpack_op and sns_T_op are 0'
		return take_op, postpack_op, sns_T_op

	def view_set(self):
		'input table_view_op and layout_view_op by 0 or 1'
		'if layout_view_op is 1, input layout image'
		'if layout_view_op is 0, layout is None'
		return table_view_op, layout_view_op, layout

	def input_set(self):
		'input request_op and sns_op by 0 or 1'
		return request_op, sns_op

	def menu_set(self):
		'input the add or delete or mod in option'
		if option == 1:
			self.menu.append(menu())
		elif option ==2:
			'input menu index for mod'
			self.menu[index].mod()
		else:
			'input menu index'
			self.menu.pop(index)

	def table_set(self):
		'input the add or delete in option'
		if option:
			'input the table information'
			self.table.append(seat(num, limit, pos))
		else:
			'input the index'
			self.table.pop(index)

	def wait_sys(self, name, phon):
		'input the waiting or cancel in waiting by 1 or 0'
		if waiting:
			self.Queue.append(wait(name, phon, self.layout_view_op, self.menu, len(self.Queue), self.table, self.layout, self.request_op, self.sns_op))
		else:
			'serch the waiting index by name and phon'
			a = self.Queue.pop(index)
			a.cancel()

	def reser_sys(self, name, phon):		
		'input the reservation or cancel in reservation by 1 or 0'
		if reservation:
			self.reservation.append(reser(name, phon, self.layout_view_op, self.menu, self.reservation, self.table, self.layout))
		else:
			'serch the reservation index by name and phon'
			a = self.reservation.pop(index)
			a.cancel()

	def take_sys(self, name, phon):
		self.take.append(take_out(name, phon, self.postpack_op, self.sns_T_op, self.menu, len(self.take)))

	def reset(self):
		'input PW'
		if self.PW == PW:
			'input what are you want for reset in a'
			if a == 0:
				self.PW_set()
			if a == 1:
				self.reser_set()
			if a == 2:
				self.take_set()
			if a == 3:
				self.view_set()
			if a == 4:
				self.input_set()
			if a == 5:
				self.menu_set()
			else:
				self.take_set()

	def start(self):
		while 1:
			'view the self.view information and Queue, but table_view_op is 1 view len(table) instead Queue'
			'input the information of customer and, Select the reservation or take_out or waiting or reset, but waiting is view only table are full, reservation and take_out butten are depend on each option'
			if reservation:
				self.reser_sys(name,phon)
			if take_out:
				self.take_sys(name,phon)
			if waiting:
				self.wait_sys(name,phon)
			if reset:
				self.reset()