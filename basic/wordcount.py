#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def word_count(filename):
  """
  brute force list break down
  """
  # test_list = []
  # test1 = []
  # test2 = []
  # test3 = []
  # test4 = []
  # test5 = []
  # f = open(filename, 'r')
  # for word in f:
  #   test_list.append(word)
  # test1, test2, test3, test4, test5 = test_list
  # new_test_list = test1 + test2 + test3 + test4 + test5
  # print len(new_test_list.split(' '))
  # print len(new_test_list)
  # f.close()
  

  """
  not brute force list break down
  """
  # test_list = []
  # f = open(filename, 'r')
  # for word in f:
  #   test_list.append(word.split(' '))
  # print len(test_list)
  # f.close


  """
  read function and printing of count of individual word
  """
  # test_list = []
  # test_list_1 = []
  # test_list_2 = []
  # count = 0
  # f = open(filename, 'r')
  # test_list = f.read()
  # new_test_list = test_list.lower()
  # new_test_list_lower = new_test_list.split()
  # # print new_test_list_lower
  # for word in new_test_list_lower:
  #   if word == new_test_list_lower[5]:
  #     count += 1
  # print new_test_list_lower[5],' = ', count

  """
  minimized convertion of lower and split. with "almost" word count
  """
  dict1 = {}
  f = open(filename, 'r')
  list1 = f.read()
  words = list1.lower().split()
  for word in words:
    dict1[word] = dict1.get(word,0) + 1
    # if word not in dict1:
    #   dict1[word] = 1
    # else:
    #   dict1[word] += 1
  return dict1
  # for k in sorted(test_dict.keys()):
  #   print k, test_dict[k]
  # return test_dict

def print_words(filename):
  word_count_dict = word_count(filename)
  for k in sorted(word_count_dict.keys()):
    print k, word_count_dict[k]

def top_20(v):
  return v[1]

def print_top(filename):
  word_count_top = word_count(filename)
  # print Counter(word_count_top).most_common(20)
  """
  Mk.1*** shortened version using lambda and [0:20] at the end of the sorted() funciton
  """
  # top_20 = sorted(word_count_top.items(), key=lambda x: x[1], reverse=True)[0:20]
  # for item in top_20:
  #   print "{0}: {1}".format(*item)

  """
  Mk.2*** using a custom function to make a custom sorted() function top_20. actual solution for activity
  """
  items = sorted(word_count_top.items(), key=top_20, reverse=True)
  for item in items[0:20]:
    print item[0], item[1]


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
