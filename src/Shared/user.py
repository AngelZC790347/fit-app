class User(object):
	"""docstring for User"""
	def __init__(self, dni, name, last_name, email):
		super(User, self).__init__()
		self.dni = dni
		self.name = name
		self.last_name = last_name
		self.email 	= email
	