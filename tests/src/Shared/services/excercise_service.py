import unittest
from src.Shared import *
class ExcerciseServiceTest(unittest.TestCase):
	"""docstring for ExcerciseService"""
	def setUp(self):
		self.es = ExcerciseService()
	
	def test_get_one(self):
		self.assertTrue(isinstance(self.es.get_excersice_by_id(1),Excercise))	