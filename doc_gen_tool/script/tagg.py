#don't need to worry about tags inside of other tags scenarios, as this doesn't make sense to type in the first place.

#-----
#TAG EVALUATION FUNCTIONS
#-----


import re
import funcs
class Tagg:
	"""
	Class for running code tags in text.

	members:
	init_str: unparsed string
	t_str: parsed string - code in string tags has been run.
	"""

	def __init__(self,init_str):
		self.delim1 = '{{'
		self.delim2 = '}}'
		self.init_str = init_str
		self.t_str = self.tag_eval()

	def tag_eval(self):
		#can replace above to function calls with special delim function calls.
		pattern = re.escape(self.delim1) + '(.*?)' + re.escape(self.delim2)
		prev_t_str = ""
		self.t_str = self.init_str
		while prev_t_str != self.t_str:
			prev_t_str = self.t_str
			self.t_str = re.sub(pattern,self.eval_tag,self.t_str)
		return self.t_str

	def eval_tag(*match_obj):
		"""returns eval'd group 1 from regex"""
		#For some reason we pass two arguments in instead of one, and the first argument is this Tagg object. There is probably a better fix than this, but not worth investigating right now.
		return eval(match_obj[1].group(1))


#----------
#tag file functions

import os
def tag(form_file):
	"""returns parsed form_file"""
	root_path = os.path.abspath(os.pardir)
	form_file = root_path + '/forms/' + form_file
	with open(form_file,'r') as fin:
		t = Tagg(fin.read())
	return t.t_str

def tag_str(t_str):
	t = Tagg(t_str)
	return t.t_str
