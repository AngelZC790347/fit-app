import sqlite3
import unittest
from src.Pots.excercise_manager import ExcerciseController

class ExcerciseControllerTest(unittest.TestCase):
    def setUp(self):
        self.exc_c = ExcerciseController(1,12,3,43)

    def test_default_exc_name(self):
        self.assertEqual(self.exc_c.id,1)
