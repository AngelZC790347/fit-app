import sqlite3
from ..Shared import ArgTypeExecption
from ..Shared.excercise import Excercise


class ExcerciseCreator():	
	__data = "data.db"

	def __BuildQuery__(self, name: str = None, id_e: int = None)-> str:
		if name == None and id_e == None:
			raise ArgTypeExecption("Invalid Argument Type from query")
		query= f"insert into excercises (name) values ('{name}');" if name != None else f"delete from excercises where id = {id_e};"
		return query
	
	def __GetRowCount__(self, query:str):
		connection = sqlite3.connect(self.__data)
		connection.row_factory = sqlite3.Row
		res = connection.execute(query)
		connection.close()
		return res.rowcount
	
	def __CreateExcercise__(self, name: str):
		return self.__GetRowCount__(self.__BuildQuery__(name))
	
	def __DeleteData__(self, id_e: int):
		return self.__GetRowCount__(self.__BuildQuery__(id_e=id_e))
		