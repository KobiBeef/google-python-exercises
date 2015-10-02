import sys
import re
import os
import shutil
import commands

"""
Mk.1*** making a new directory
"""

# directory = sys.argv[1]
# new_path = '/secret_files'
# secret_files = os.makedirs(directory + new_path, 0777)
# print 'directory made'

# filenames = os.listdir(directory)
# print filenames\

"""
Mk.2*** finding the files (\w+__\w+__) and listing thier absolute new_path
"""
# print type(filenames)
# files = re.search(r'(\w+__\w+__)', filenames)
# for files in filenames:
# 	secret_file = re.findall(r'(\w+__\w+__)', files)
# 	if secret_file not in test:
# 		test.append(secret_file.group())

# print test		
# print files.group(1)


# for files in filenames:
# 	secret_files = re.findall(r'(\w+__\w+__.\w\w\w)', files)
# 	if secret_files not in test:
# 		test.append(secret_files)

# print test
# *** looking to separate the secretfiles
# for files in filenames:
# 	secret_files = re.findall(r'(\w+__\w+__.\w\w\w)', files)
# 	if secret_files not in test:
# 		test.append(secret_files)

# test.pop(0)
# print test

"""
Mk.3*** copying secret files to new directory
"""
# destination = filenames + new_folder
# new_folder = '/secret_files'
# new_files = os.makedirs(directory + new_folder, 0777)

# for files in test:
# 	shutil.copy(test, new_files)
# 	pass

# for filename in filenames:
# 	path = os.path.abspath(filename)
# 	print path
"""
Mk.4*** (FINAL for getting full path) extracting the secret file more cleaner
"""
# secret_files = []
# for files in filenames:
# 	# files = files.rstrip()
# 	if re.search(r'__\w+__', files):
# 	#*** checking to see if it finds the secretfiles
# 		path = os.path.abspath(files)
# 		if path not in secret_files:
# 			secret_files.append(path)

# return secret_files

"""
Mk.1*** for copying special files in made manualy directory
"""
# directory = sys.argv[1]
# destination = sys.argv[2]
# *** dont need this: *** source = os.path.abspath(directory)
# filenames = os.listdir(directory)
# special_files = []
# for files in filenames:
# 	if re.search(r'__\w+__', files):
# 		shutil.copy(files, destination)


"""
Mk.2*** make new directory for the copied files
"""
directory = sys.argv[1]
destination = sys.argv[2]
filenames = os.listdir(directory)
special_files = []
new_directory = os.makedirs(destination, 0777)
for files in filenames:
	if re.search(r'__\w+__', files):
		shutil.copy(files, destination)

# shutil.copy(special_files, destination)


# for reference of main pattern for sys.argv
# python copyspecial.py --todir   '\test'   .
# sys.argv  [0]            [1]      [2]    [3]
# python copyspecial.py   --todir  '\test'   .
# args = sys.argv[1:]       [0]      [1]    [2]
                         # args[0]  todir special_files
