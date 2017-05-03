import os

from shutil import copyfile, copytree



if __name__ == '__main__':
	BASE_PATH = '/home/{}/'.format(os.getlogin())
	CORE_PATH = "{}.buildscripts/".format(BASE_PATH)
	SUB_PATH = "{}/config/".format(CORE_PATH)
	install_path = 'config/'
	base_files = ('head.html', 'foot.html', 'buildscript.py',
	              'content_functions.py', 'merge.py')
	try:
		exists = (False,True)[os.path.isdir(CORE_PATH)]
		print(exists)
		basexists = (False,True)[os.path.isdir(SUB_PATH)]
		print(basexists)
		if not exists or not basexists:
			try:
				print("making dir at {}".format(CORE_PATH))
				os.mkdir(CORE_PATH)
			except FileExistsError:
				pass
			try:
				print("Makeing dir at {}".format(SUB_PATH))
				os.mkdir(SUB_PATH)
			except FileExistsError:
				pass
			for file in base_files:
				if file not in os.listdir(SUB_PATH):
					print("Copying files...")
					copyfile(install_path+file,SUB_PATH+file)
	except Exception as e:
		raise e
"""
	user = os.getlogin()
	alias_merge = "alias merge-static='python3 /home/{}/.buildscripts/config/merge.py'\n".format(user)
	alias_build = "alias build-static='python3 /home/{}/.buildscripts/config/buildscript.py'\n".format(user)

	print("Creating an alias for merge and build...")
	with open('/home/{}/.bashrc'.format(os.getlogin()), 'a') as bash:
		bash.write(alias_merge)
		bash.write(alias_build)
"""
