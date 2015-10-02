#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_path(path):
  secret_files = []
  filenames = os.listdir(path)
  for files in filenames:
    # files = files.rstrip()
    if re.search(r'__\w+__', files):
    #*** checking to see if it finds the secretfiles
      path = os.path.abspath(files)
      if path not in secret_files:
        secret_files.append(path)

  return secret_files

def to_directory(todir, special_files):
  # directory = sys.argv[1]
  # destination = sys.argv[todir]
  # filenames = os.listdir(special_files)
  # using the get_path function to find the special files
  filenames = get_path(special_files)
  new_directory = os.makedirs(todir, 0777)
  for files in filenames:
    shutil.copy(files, todir)
  
  # ----------------------------------------


def tozip():
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  
  # *** when input in powershell is 'python copyspecial.py .'
  path = ''
  if args[0] == '.':
    path = args[0]
    full_path = '\n'.join(get_path(path))
    print full_path
    # del args[0:2]
      
  todir = ''
  special_files = ''
  if args[0] == '--todir':
    todir = args[1]
    special_files = args[2]
    to_directory(todir, special_files)
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()