import os,re
import argparse
from shutil import copyfile
from content_functions import warning_message, creating_message

MESSAGES = {"WARNING" : "WARNING: FILE {} MISSING. EXITING.",
			"CHECKING": "Checking current directory for minimum build files...",
			"CREATNG" : ("Creating static html files in parent directory:", "="),
			"SKIPPING": "Skipping  {}",
			"CLEANING": "Cleaning up files...",
			}
dir_content = {"contents"         : os.listdir(os.getcwd()),
		       "parentContents"   : os.listdir(os.path.abspath(".."))}


if __name__ == '__main__':
	parse = argparse.ArgumentParser()
	parse.add_argument('PROJECTNAME', required=True, help="Give the name of the project")
	parse.add_argument('PATH', required=True, help="Give the path of the new project")
	args = parse.parse_args()

	if not args.PROJECTNAME or not args.PATH:
		exit(0)
	else:
		project = args.PATH+'/'+args.PROJECTNAME
		#Create the directory
		os.mkdir(project)
		print(creating_message(message="Creating {}".format(project), dec="="))
		#create sub dirs main and config
		os.mkdir(project+'/main')
		os.mkdir(project+'/config')
		base_file= '/home/{}/.buildscripts/config/'.format(os.getlogin())
		contents = os.listdir(base_file)
		for file in contents:
			copyfile(base_file+file, project+'/config/')

		print(creating_message(message="Finished", dec="+=+"))