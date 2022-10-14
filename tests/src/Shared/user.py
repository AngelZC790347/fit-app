import unittest
from src.Shared import *
class UserTest(unittest.TestCase):

	def setUp(self):
		self.usr = User(12,"angel","","test@test.gmail")

	def test_create(self):
		self.assertEqual(self.usr.name.upper(),"ANGEL")
		self.assertTrue(isinstance(self.usr,User))		