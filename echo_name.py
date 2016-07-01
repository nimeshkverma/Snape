#!/usr/bin/python

import pprint

name = raw_input("What\'s your name?\n")
name = name.strip()
#pprint.pprint(ranu)
#exit()
flag = 1;
while flag :	
	if not name:
		print "Incorrect input. Please enter 'py'\n"
		name = raw_input("Please enter 'py'\n")
		name = name.strip()
	else :
		if name.lower() == 'py':
			flag = 0
		else:
		
			print "Incorrect input\n"
			name = raw_input("Please enter 'py'\n")
			name = name.strip()
data = { 
"p" : '''
_____
||  ||
||__||
||
||
''',
"y" : '''
||  ||
||__||
    ||
    ||
||__||
'''
}
res = ''
for i in name :
	res = res + data[i]
print res
exit()
