import sqlite3
from sqlite3 import Cursor
from ..Shared import *
class ExcerciseController(ExcerciseService,Excercise):
	"""docstring for ExcerciseController"""
	def __init__(self,id_e,reps,series,w_kg):
		tmp_E = self.get_excersice_by_id(id_e)
		if tmp_E != None:
			super(ExcerciseController, self).__init__(tmp_E.id,tmp_E.name)
			self.reps 	= reps
			self.series = series
			self.w_kg 	= w_kg
			
		