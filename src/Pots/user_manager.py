from ..Shared import *
class UserController(User,UserService):
	"""docstring for UserController"""
	def __init__(self, dni):
		tmp_u = self.get_user_by_id(dni)
		if tmp_u != None:
			super(UserController, self).__init__(tmp_u.dni,tmp_u.name,tmp_u.last_name,tmp_u.email)
		else:
			self.name = None
			self.last_name = None	