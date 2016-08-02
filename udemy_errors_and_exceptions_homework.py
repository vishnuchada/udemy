#!/usr/bin/python
from __future__ import division

try:
	for i in ['a','b','c']:
		print i**2
except:
	print "There was an error"

#####
try:
	x = 5
	y = 0
	z = x/y
except:
	print "there was a zerodivision error"
finally:
	print "All done"

#####
def ask():
	while True:
		try:
				n = int(raw_input('please enter an integer : '))
		except:
			print "An error occurred! Please try again"
			continue
		else:
			break
			
	print 'Thank your, your number squared is : ',n**2

ask()
