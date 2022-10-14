import sqlite3
from sqlite3 import Cursor,Row
from ..user import User
SQLITE_ROOT = "/Users/angelcano/Documents/Sublime/Aplicaciones_Python/back-up/data.db"
class UserService(object):
	"""docstring for UserService"""
	def get_user_by_id(self,dni)-> User:
		connection = sqlite3.connect(SQLITE_ROOT)
		cursor	   = connection.cursor()
		connection.row_factory = sqlite3.Row
		try:
			res = connection.execute(f"select * from users where dni = {dni};").fetchone()
		except sqlite3.OperationalError as o_error:
			raise o_error
		else:	
			connection.commit()
			if res != None :
				return User(res['dni'],res['name'],res['lastname'],res['email'])
		finally:
			connection.close()