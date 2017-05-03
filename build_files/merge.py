"""Merge.py
Merges all files with a .html file extension that are not header || footer

You can specify what files you want merged, if nothing is specified it merges all the 
files that meet the parameters.

"""
import os
from shutil import copyfile



if __name__ == '__main__':
	files_ = os.listdir(os.getcwd())
	content_dir = os.getcwd()+'/main'
	base_files = ('head.html', 'foot.html')
	path_main = os.getcwd()+'/main/'
	files = [f for f in files_ if f not in base_files if f[-5:] == '.html']
	for content in os.listdir(path_main):
		os.remove(path_main+content)

	for file in files:
		fstruct = [base_files[0],file,base_files[1]]
		if file not in os.getcwd()+'/main':
			os.popen('touch main/{}'.format(file))
		else:
			open(os.getcwd()+'/main/'+file, 'w').close()
		with open(os.getcwd()+'/main/'+file, 'a') as ofile:
			for struct in fstruct:
				try:
					with open(os.getcwd()+'/'+'config'+'/'+struct,'r') as s:
						s = s.readlines()
						for line in s:
							ofile.write(line)
				except FileNotFoundError:
					with open(struct, 'r') as s:
						s = s.readlines()
						for line in s:
							ofile.write(line)




#todo: issue--file if it exists gets doubled. need to delete contents of the file then append the bs
