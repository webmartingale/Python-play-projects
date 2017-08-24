#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename)
  text = f.read()
  f.close()
  
  #year
  reg_year = r'Popularity\sin\s(\d\d\d\d)</h'
  match = re.search(reg_year, text)
  if match:
    year = match.group(1)
  #print year
  #names
  names = {}
  reg_names = r'tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
  #match = re.search(reg_names, text)
  #if match:
  #  print match.group()
  
  tuples = re.findall(reg_names, text)
  #if tuples:
  #  print tuples[0]
  
  for tuple in tuples:
    nr = tuple[0]
    name1 = tuple[1]
    name2 = tuple[2]
    #print nr, name1, name2
    
    if name1 in names:
      if names[name1] < nr:
        names[name1] = nr
    else:
      names[name1] = nr
    if name2 in names:
      if names[name2] < nr:
        names[name2] = nr
    else:
      names[name2] = nr
      
  #build rank list
  ranklist = [year]
  for name in sorted(names.iterkeys()):
    ranklist.append(name + ' ' + names[name])
  #print ranklist[0:10]  
  return ranklist

def print_ranklist(ranklist):
  for item in ranklist:
    print item

def write_ranklist(ranklist, filename_orig):
  fw = open(filename_orig+'.summary', 'w')
  for item in ranklist:
    fw.write(item+'\n')
    
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:  
    ranklist = extract_names(filename)
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    if summary:
      write_ranklist(ranklist, filename)
    else:
      print_ranklist(ranklist)
    
if __name__ == '__main__':
  main()
