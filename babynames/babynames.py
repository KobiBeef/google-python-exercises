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
  # +++your code here+++

  """
  Mk.4*** in action
  """
  # *** reading each line in f and checking the regular expression and storing it in a list
  # for lines in f:
  #   lines = lines.rstrip()
  #   y = re.findall('in (\d\d\d\d)', lines)
  #   d = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', lines)
  #   if len(y) > 0:
  #     year = y
  #   elif len(d) > 0:
  #     initial_list.append(d)
  
  # # *** segregating the data in initial_list into key and values and storing in into a dictionary
  # for data in initial_list:
  #   for value in data:
  #     initial_dict[value[0]] = value[1], value[2]
      
  # # *** separating the two values from the intial_dict and storing the value and its corresponding key into a list
  # for key, values in initial_dict.items():
  #   for value in values:
  #     names_rank = value +' '+ key
  #     list_names_rank.append(names_rank)

  # # *** putting the year on top of the list
  # final = year + list_names_rank

  # # *** printing the year and the final list
  # for names in sorted(final):
  #   print names
  """
  Mk.5*** in action
  """
  f = open(filename, 'rU')
  texts = f.read()
  names = []
  initial_dict = {}

  year = re.search(r'Popularity\sin\s(\d\d\d\d)', texts)
  if not year:
    sys.stderr.write('Cant find year \n')
    sys.exit(1)

  names.append(year.group(1))

  data = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', texts)
  for values in data:
    key, value1, value2 = values
    if value1 not in initial_dict:
      initial_dict[value1] = key
    if value2 not in initial_dict:
      initial_dict[value2] = key

  for name in sorted(initial_dict.keys()):
    names.append(name + ' ' + initial_dict[name])

  return names


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

  """
  Mk.1*** adding condition for direct extraction html file with out the '--summaryfile' line like in the solution typing 'python babynames.py baby1990.html' would result in the whole list of names arranged aphabetically.
  """
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
 
# *** getting the filename by checking each entry in the list
  for filename in args:
    names = extract_names(filename)

    # if summary:
    #   f = open(args[0]+.'summary', 'w')

    text = '\n'.join(names)

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text)
      outf.close()
    else:
      print text

# *** getting the filename when it is typed
  # if args[0] == args[0]:
  #   extract_names(args[0])
  
if __name__ == '__main__':
  main()
