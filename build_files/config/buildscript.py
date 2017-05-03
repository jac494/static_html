import re

from shutil import copyfile
from .content_functions import warning_message,creating_message

MESSAGES = {"WARNING" : "WARNING: FILE {} MISSING. EXITING.",
			"CHECKING": "Checking current directory for minimum build files...",
			"CREATNG" : ("Creating static html files in parent directory:", "="),
			"SKIPPING": "Skipping  {}",
			"CLEANING": "Cleaning up files...",
			}
dir_content = {"contents"         : os.listdir(os.getcwd()),
		       "parentContents"   : os.listdir(os.path.abspath(".."))}


############################CHECK FOR FILES#####################################
special_files = set('buildscript.py', 'head.html', 'foot.html')
hiddenFiles = re.compile('^\.')
print(MESSAGES["CHECKING"])
######CHECK FOR INTERSECTIONS
inter_c,inter_h = (dir_content['special_files'] & set(dir_content['contents']),
	dir_content['special_files'] & set([file_ for file_ in dir_content['contents']
				if hiddenFiles.match(file_)]))
if len(inter_c) >=1 or len(inter_h)>=1:
	garbage = warning_message(message=MESSAGES["WARNING"])
garbage = creating_message(message=MESSAGES["CREATING"][0],
						   dec=MESSAGES["CREATING"][1])
inter_p = set(dir_content["parentContents"]) & set(dir_content["contents"])
if len(inter_p) >=1:
	cleaning = [os.remove(os.path.abspath('..')+'/'+file_) for file_ in inter_p]
	print("Cleaned {}".format(file_ for file_ in inter_p))	#REVIEW: replace with dict
###############################################################################

print("{}\ncreating file {}".format(outFile,outFile))
input_file_list = ["head.html", file_, "foot.html"]
#open each file in input_file_list and write the contents of the outFile



#######check for updates
#when code block is run, it will take any changes in '.html' file extensions
