from sys import argv
import sys 
import re


# test_dict = {}
initial_dict = {}
script, filename = argv
f = open(filename, 'rU')
texts = f.read()
# f = open(filename)
# test_list = []
initial_list = []
# female_dict = {}
# male_dict = {}
names = []
# sorted_names = []
# final = []
list_names_rank = []
"""
JUNK_TEST1
"""
# lst = texts.read()
# for line in texts:
# 	line = line.rstrip()
# 	if re.findall('\S+@\S+', line):
# 		print line

# emails = re.findall('\w+@\S+\w', lst)
# print texts
"""
Mk.1*** putting the year and rank in a list
"""

# for line in texts:
# 	line = line.rstrip()
# 	y = re.findall(' in (\d+)<', line)
# 	r = re.findall('>(\d+)<', line)
# 	if len(y) > 0:
# 		year.append(y)
# 		print y
# 	elif len(r) > 0:
# 		rank.append(r)
# 		print r

"""
JUNK_TEST2
"""
# print year
# print rank

# for line in texts:
# 	line = line.rstrip()
# 	r = re.findall('>(\d+)<', line)
# 	if len(r) > 0:
# 		print x


# s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print lst
"""
Mk.2*** trying to store the rank, male and female names into one list
"""
# for line in texts:
# 	line = line.rstrip()
# 	n = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
# 	if len(n) > 0:
# 		names.append(n)
# print names
"""
Mk.3*** trying to store the year, rank female and male names into one dictonary
"""
# this
# for line in texts:
# 	line = line.rstrip()
# 	y = re.findall('in (\d\d\d\d)', line)
# 	x = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
# 	if len(y) > 0:
# 		year = y
# 	elif len(x) > 0:
# 		test_list.append(x)



# *** printing sorted male and female
# print sorted(male_dict.items(), key=lambda x: x[1]) + sorted(female_dict.items(), key=lambda x: x[1])


# this
# *** storing rank, male name, and female name in one dict
# for list1 in test_list:
# 	for word in list1:
# 		test_dict[word[0]] = word[1], word[2]
		# print sorted(word[1]), word[2]



# *** getting each value and key
# for n in test_dict.values():
# 	for x in n:
# 		print x, test_dict[x]

# *** separating the 2 values and adding the key
# for k, v in test_dict.items():
# 	for n in v:
# 		print n, k


# this
# *** storing names and rank in a list
# for k, v in test_dict.items():
# 	for n in v:
# 		sorted_names = n +' '+ k
# 		final.append(sorted_names)
# **** joining year and sorted names and ranks
# ultima = year + final


# this
# *** for year and aphabetically arranged names
# for name in sorted(ultima):
# 	print name


	
# for value in sorted(sorted_names.values()):
# 	print value

# *** testing to append a dict into a list
# for n in test_dict.values():
# 	for x in n:
# 		names.append(x)
# 		sorted_names = sorted(names)
# print sorted_names
"""
Mk.4*** proper naming of the variables and cleaning the code
"""
# *** reading each line in f and checking the regular expression and storing it in a list
# for lines in f:
# 	lines = lines.rstrip()
# 	y = re.findall('in (\d\d\d\d)', lines)
# 	d = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', lines)
# 	if len(y) > 0:
# 		year = y
# 	elif len(d) > 0:
# 		initial_list.append(d)

# # *** segregating the data in initial_list into key and values and storing in into a dictionary
# for data in initial_list:
# 	for value in data:
# 		initial_dict[value[0]] = value[1], value[2]
	 	
# # *** separating the two values from the intial_dict and storing the value and its corresponding key into a list
# for key, values in initial_dict.items():
# 	for value in values:
# 		names_rank = value +' '+ key
# 		list_names_rank.append(names_rank)

# # *** putting the year on top of the list
# final = year + list_names_rank

# # *** printing the year and the final list
# for names in sorted(final):
# 	 print names

"""
Mk.5*** shortening of code for more efficient run from google solution
"""
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

print names