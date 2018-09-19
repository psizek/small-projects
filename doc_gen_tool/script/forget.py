#forget - FORm GEneration Tool

#-----
#FORMS
#-----

#Form
#desc: contains members for setting forms
#members:
#init_str - this is the unparsed string.
#t_str - this is the parsed string.
#form_dict - this defines which form substitutions to make.

import re
class Form:

	def __init__(self,init_str,form_dict): #make form_dict optional??
		self.delim1 = '[['
		self.delim2 = ']]'
		self.delim_mid = '##'
		self.init_str = init_str
		self.form_dict = form_dict
		self.form_eval()

	def add(self,key,value):
		form_dict[key] = value
	def delete(self,key):
		del form_dict[key]

	#form_eval
	#desc: given a string and args, attempts to perform regex replacements to fill in the form. Matches on <delim1><tag><delim_mid><default><delim2>. Right now, these can only span a single line.
	def form_eval(self):

		prev_t_str = ""
		self.t_str = self.init_str
		while prev_t_str != self.t_str: #run in case more tags pop up.
			prev_t_str = self.t_str
			for tag in self.form_dict:
				r_str = self.form_dict[tag]
				pattern = re.escape(self.delim1) + tag + re.escape(self.delim_mid) + '((.|' + re.escape('\n') + ')*?)' + re.escape(self.delim2)
				self.t_str = re.sub(pattern,r_str,self.t_str)

		#cleanup missing tags.
		pattern = re.escape(self.delim1) + '.+?' + re.escape(self.delim_mid) + '((.|' + re.escape('\n') + ')*?)' + re.escape(self.delim2)
		self.t_str = re.sub(pattern,'\\1',self.t_str)

		return self.t_str


#---------
#file operations
#form
#desc: generates a return string from form function.
#params:
#form_file: file which we use for replacements
#form_dict: how to perform form replacements.
import os
def form(form_file,form_dict):
	root_path = os.path.abspath(os.pardir)
	form_file = root_path + '/forms/' + form_file
	with open(form_file,'r') as fin:
		f = Form(fin.read(),form_dict)
	return f.form_eval()

#form_x
#desc: same as above, except assumes all tags in the form are number, and uses the additional arguments in *args to fill out those tag values.
#params:
#form_file: file which we use for replacements
#*args: optional arguments which contain the form entries for the file in question, by number.
def form_x(form_file,*args):
	count = 0
	for arg in args:
		count += 1
		form_dict[str(count)] = str(arg)
	return form(form_file,form_dict)
