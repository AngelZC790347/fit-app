import sqlite3
import unittest
from src.BackOffice.excercise_manager import ExcerciseCreator

class ExcerciseCreatorTest(unittest.TestCase): 
    def test_NewExcercise(self):
        self.assertEqual(ExcerciseCreator().__CreateExcercise__("peso muerto rumano"),1)

    def test_Delete(self):
        self.assertEqual(ExcerciseCreator().__DeleteData__(1),1)    