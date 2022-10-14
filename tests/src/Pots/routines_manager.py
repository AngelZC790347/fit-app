import sqlite3
import unittest
from src.Pots.routines_manager import RoutineController

class RoutineControllerTest(unittest.TestCase):
    def setUp(self):
        self.r_c = RoutineController(12,'push')

    def test_default_exc_name(self):
        self.assertEqual(self.r_c,None)
