import cmd
import os,sys

def constructor(self,intro,opts):
		self.intro = intro 
		self.opts = opts

def getpass(prompt="Password: "):
    import termios, sys
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd

def build_iCli(intro:str,opts:dict):
	it=opts.keys()
	tmp_opt={'do_'+x.strip().replace(' ',''):opts[x] for x in it}
	tmp_opt['__init__']=constructor
	IAdminCli=type('IAdminCli',(cmd.Cmd,),tmp_opt)
	return IAdminCli(intro,it)
	# print(10*"#"+self.intro+10*"#")
	# for opt in self.menu_opt:
	# 	print(opt)
	# usr_opt = input("Select Option ")
	# print(usr_opt) 

if __name__ == '__main__':
	menu_opt = {"Pots":1
		,"Data Base":2
		,"Show Metrics":3
		,"Salir":0}
	newTools=build_iCli("Admin Tools",menu_opt)
	print(10*"#"+newTools.intro+10*"#")
	for opt in newTools.opts:
		print(opt)
	usr_opt = input("Select Option -> ")
	print(usr_opt)