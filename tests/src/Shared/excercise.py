import unittest
from src.Shared.excercise import Excercise
class ExcerciseTest(unittest.TestCase):

	def setUp(self):
		self.exc = Excercise(12,"Cardio")

	def test_create(self):
		self.assertEqual(self.exc.name.upper(),"CARDIO")
		self.assertTrue(isinstance(self.exc,Excercise))			
		