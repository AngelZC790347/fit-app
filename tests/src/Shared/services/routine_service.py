import unittest
from src.Shared import *
class RoutineServiceTest(unittest.TestCase):
	"""docstring for ExcerciseService"""
	def setUp(self):
		self.rs = RoutineService()
	
	def test_get_one(self):
		self.assertTrue(isinstance(self.rs.get_routine_by_id(1),dict))	