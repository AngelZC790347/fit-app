import sqlite3
import unittest
from src.Pots.user_manager import UserController

class UserControllerTest(unittest.TestCase):
    def setUp(self):
        self.usr_c = UserController(76608998)

    def test_default_exc_name(self):
        self.assertEqual(self.usr_c.name,'Angel')
