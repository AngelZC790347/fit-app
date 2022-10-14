from .excercise_manager import ExcerciseController
from .user_manager import UserController
from ..Shared import *
class RoutineController(RoutineService,object):
	"""docstring for RoutineController"""
	def __init__(self,id_r,name):
		self.res=self.get_routine_by_id(id_r)
		if self.res != None:
			self.usr_c = UserController(res['usr_dni'])
		super(RoutineController, self).__init__()