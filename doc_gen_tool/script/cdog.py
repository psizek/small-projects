#import statements
import forget
import tagg

#--------------------
#usercode goes here:

#e.g.

my_dict = {'color' : 'blue'}

t_str = forget.form('test_form', my_dict)

t = tagg.Tagg(t_str)
t_str = t.t_str

#export data:
import os
root_folder = os.path.abspath(os.pardir)
output_file = 'test'
output_file = root_folder + '/output/' + output_file
with open(output_file, 'w') as fout:
	fout.write(t_str)
