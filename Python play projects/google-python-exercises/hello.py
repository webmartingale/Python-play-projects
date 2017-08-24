#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
print 'Github rocks!'
a = 2
print 'Outermost statements run first! :)'
a = a + 4
print 'Contents of __name__: ', __name__
print 'Type of __name__: ', type(__name__)

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    z = sys.argv[0]
    name = sys.argv[1]
  else:
    name = 'World'
  print 'Argv[0]: ', z
  print 'Hello', name
  print a
  #main2() #does not work, needs to be defined earlier.

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
  #main2() #does not work, needs to be defined earlier.
  
def main2():
	print 'main2()'