from .services.excercise_service import ExcerciseService
from .services.user_service import UserService
from .services.routine_service import RoutineService
from .excercise import Excercise
from .user import User
class ArgTypeExecption(Exception):
	"""docstring for ArgTypeExecption"""
	pass

__all__ = [
	"Excercise"
	,"User"
	,"ExcerciseService"
	,"UserService"
	,"RoutineService"
]	
		