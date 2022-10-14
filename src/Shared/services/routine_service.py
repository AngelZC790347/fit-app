import sqlite3
from sqlite3 import Cursor,Row

SQLITE_ROOT = "/Users/angelcano/Documents/Sublime/Aplicaciones_Python/back-up/data.db"
class RoutineService(object):
	"""docstring for RoutineService"""
	def get_routine_by_id(self,id_r)-> {}:
		connection = sqlite3.connect(SQLITE_ROOT)
		cursor	   = connection.cursor()
		connection.row_factory = sqlite3.Row
		res 	  = connection.execute(f"select * from routines where id = {id_r};").fetchone()
		connection.commit()
		connection.close()
		if res != None:
			return {res['id'],res['usr_dni'],res['name']}
