#!/bin/python3
#------ imports --------
import sys
import os
import re

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


special_files = ['buildscript.py', 'head.html', 'foot.html']
dir = os.getcwd()
parentDir = os.path.abspath('..')
contents = os.listdir(dir)
print("Checking current directory for minimum build files...")
for file in special_files:
    if file in contents:
        continue
    else:
        sys.stdout.write(REVERSE + RED)
        print("WARNING: FILE", file, "MISSING. EXITING.")
        sys.stdout.write(RESET)
        exit()
parentContents = os.listdir(parentDir)
hiddenFiles = re.compile('^\.')

sys.stdout.write(REVERSE + GREEN)
print("\n")
print("=================================================")
print("Creating static html files in parent directory...")
print("=================================================")
print("\n")

sys.stdout.write(RESET)
for file in contents:
    if file in special_files or hiddenFiles.match(file):
        sys.stdout.write(BOLD)
        print("skipping file", file)
        sys.stdout.write(RESET)
    else:
        if file in parentContents:
            print("  Cleaning ", file, " from parent directory.")
            parentPathFile = parentDir + "/" + file
            os.remove(parentPathFile)
        outFile = os.path.join(parentDir, file)
        print(outFile)
        print("creating file", outFile)
        inputFileList = ["head.html", file, "foot.html"]
        for inputFile in inputFileList:
            with open(inputFile) as iFile:
                with open(outFile, "a+") as oFile:
                    for line in iFile:
                        oFile.write(line)

print("\n")
