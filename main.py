import unittest
import argparse,os
from pathlib import Path
from src.BackOffice import *

class ModuleHandlerAction(argparse.Action):
	def __init__(self, option_strings, dest, nargs=None, **kwargs):
		if nargs is not None:
			raise ValueError("nargs not allowed")
		super().__init__(option_strings, dest, **kwargs)

	def __call__(self, parser, namespace, values, option_string=None):
		regex = self.dest.replace('_','/')
		print(regex)
		for path in sorted(Path().rglob(regex)):
			print(path)
			p = Path.cwd() /path/ Path(values +'.py')
			if not p.is_file():
				p.touch()	
			# 	raise AttributeError("Invalid the argument must be str")	
		print('%r %r %r %r' % (namespace, values, option_string,self.dest))
		setattr(namespace, self.dest, values)
		
def test_api():
	loader = unittest.TestLoader()
	l_s = []
	suite = loader.discover("tests/src/", pattern = "*.py") 
	l_s.append(suite)
	alltests = unittest.TestSuite(l_s)
	unittest.TextTestRunner(verbosity=2).run(alltests)

def run(test_mode:bool):
	if test_mode:
		test_api()
	else:
		pass

if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument("--test","-t",action='store_true')
	parser.add_argument("--src-Pots","--sp", action=ModuleHandlerAction)
	parser.add_argument("--src-Shared","--s2", action=ModuleHandlerAction)
	parser.add_argument("--src-Shared-services","--s3", action=ModuleHandlerAction)
	args = parser.parse_args()
	run(args.test)
	
