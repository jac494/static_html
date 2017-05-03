import os,sys

from functools import wraps
from stat import S_ISDIR



# stackoverflow link with answer for coloring:
# http://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python
# ----- colors ---------
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

RPATH = os.listdir(os.path.abspath(
        '/home/{}/.build_files/config/'.format(os.getlogin())))


def style(fg,bg):
	sys.stdout.write(fg + bg)
	def funcdec(func):
		@wraps(func)
		def inner(message,dec=None):
			out,reset = func(message)
			print(out)
			sys.stdout.write(reset)
			if out:	exit()
		return inner
	return funcdec



def merge(head,f,foot):
	"""used in a for loop
		takes a file and creates a tempory file to output all the data to be merged
		then deletes the original file and renames the tempory file for uniformity
	"""
	tmp = f.__str__()+'.cp'
	with open(head , 'r') as head, open('f', 'r') as src, \
			open(foot, 'r') as foot, open(tmp, 'a') as tmp:
		tmp.write(head)
		tmp.write(src)
		tmp.write(foot)
	os.remove(f)
	creating_message(message="Removing temporary files...", dec="+-+")
	os.rename(str(tmp), str(tmp[:-3]))


	#take a file and add header and footer


@style(fg=GREEN,bg=REVERSE)
def creating_message(message,dec):
	exit = False
	line_dec = dec*len(message)
	return "\n{}\n{}\n{}\n".format(line_dec,message,line_dec), exit

@style(fg=REVERSE, bg=RED)
def warning_message(message):
	exit=True
	return (message, exit)


