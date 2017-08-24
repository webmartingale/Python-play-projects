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

def get_special_paths(dir):
  abspath = os.path.abspath(dir)
  filenames = os.listdir(dir)
  reg_specialfile = r'\w*__\w+__[\w.]*'
  special_filepaths = []
  for filename in filenames:
    match = re.search(reg_specialfile, filename)
    if match:
      name = match.group()
      special_filepaths.append(os.path.join(abspath, name))
  return special_filepaths
  
def printlist(list):
  for item in list:
    print item
  
def copytodir(filelist, todir):
  if not os.path.exists(todir):    
    os.mkdir(todir)
  destpath = os.path.abspath(todir)
  for filepath in filelist:
    shutil.copy(filepath, destpath)
  
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
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
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
  filepaths = get_special_paths(args[0])
  
  if todir:
    copytodir(filepaths, todir)
  else:
    printlist(filepaths)
  
if __name__ == "__main__":
  main()
