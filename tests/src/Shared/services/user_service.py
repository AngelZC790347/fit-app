import unittest
from src.Shared import *
class UserServiceTest(unittest.TestCase):
	"""docstring for ExcerciseService"""
	def setUp(self):
		self.us = UserService()
	
	def test_get_one(self):
		self.assertTrue(isinstance(self.us.get_user_by_id(76608998),User))	