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
output_file = 'test'
with open('/home/jummcgrum/Desktop/static_simple/output/' + output_file, 'w') as fout:
	fout.write(t_str)
