import sqlite3
from sqlite3 import Cursor,Row
from ..excercise import Excercise


SQLITE_ROOT = "/Users/angelcano/Documents/Sublime/Aplicaciones_Python/back-up/data.db"
class ExcerciseService():
	"""docstring for ExcerciseService"""
	def get_excersice_by_id(self,id)-> Excercise:
		connection = sqlite3.connect(SQLITE_ROOT)
		cursor	   = connection.cursor()
		connection.row_factory = sqlite3.Row
		res 	   = connection.execute(f"select * from excercises where id = {id}").fetchone()
		connection.commit()
		connection.close()
		return Excercise(res['id'],res['name'])
		