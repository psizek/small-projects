#This should be a list of functions that ought to be included for parsing by tagg.py

#-----------
#import statements
import forget #could be used notably for importing text from another file into this template.

#----------------
#function list

#this version doesn't support character escaping; hence the functions below:
def left_braces():
	return '{{'
def right_braces():
	return '}}'
def double_hash():
	return '##'
def left_brackets():
	return '[['
def right_brackets():
	return ']]'
