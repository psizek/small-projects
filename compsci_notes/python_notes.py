

#Python notes:

object1 is object2      #returns true if object1 is the same object as object2. Only really matters for mutable objects.
#aliasing is a thing, too (like pointers without the pointers?):
a = [1,2,3]
b = a
a is b                  #this returns true, so...
b[2] = 5                #this means that  a and b  will now look like  [1,2,5].

#Passing a list to a function will pass the REFERENCE of that list to the function, meaning the actual list object can be modified.



#Language Notes:
#typed Variables, although you don't have to type them when initializing.
#you can use underscores _ as part of a variable or function name.

#Interpreter:
#as with cache, you can run code directly at the prompt, or you can run a script
#Comments are done with:
#comment

"""some text
some text
some text"""     #this is a docstring for functions and classes

#-----
#STRINGS
#-----
'string1'       #indicates a string
"string1"       #also indicates string
'string1/n'     #indicates a newline after "string"

#characters can be grabbed from strings like:
string1[num1]              #will select the character corresponding to the num position in string. Note that '0' is position 1, '1' is two, etc.
string1[num1:num2]         #provides a slice - including the first num1 but excluding num2. you can omit num1 or num2 or both to slice it out to the furthest point
len(string1/list1)         #gives the length of a string or number of elements in a list. two letters means len(string) == 2

#strings are immutable, so you can't do string[4] = 'J'

#string methods:
string1.upper()            #gets upper case of strings
string1.find(string2)      #finds the first instance of string2 inside string1
string1.strip()            #strips whitespace from a string
string1.capitalize()       #capatalizes a string1
string1.isupper()          #returns true if a string is all uppercase.
repr(string1)              #returns a string representation of an object (useful for finding whitespace with your eyes.)

#operators
string1 in string2      #returns true if string1 is contained in string2
==                      #if two strings are equivalent
>                       #alphabetizes, likewise with <

#------
#Variables:
#------
#assignment is done via  '='
a = b       #a is assigned with b
+=          #augmented assigment -    a += b   is the same as   a = a + b

#variables can have names that aren't keywords (like class,if,and, etc.)
#variables are automatically typed when you do assignment.

#variables are local when declared inside of functions.

#There is a boolean data type.
#All non-zero numbers evaluate to True.

#Global variables are ones that can be called from any function (like an assumed variable)
#to edit global variables inside a function, you must first declare it (otherwise we create a local variable within a function):
global var1
var1 = val1
#If a variable is mutable (e.g. lists and dictionaries) you don't need to declare it first.

#-------
#OPERATORS:
#-------

#String operators:
str1 + str2      #concatonates strings

Math:
+         #addition
-         #subtraction
*         #multiplication
/         #division, probably has typing issues
**        #exponentiation
//        #floor division, rounds down to nearest integer.
%         #modulus

Logical:
==        #equals
!=        #neq
>
<
>=
<=

arg1 and arg2
or
not

#Conditionals:
if condition1:
  code1
elif condition1:
  code1
elif condition1:
  code1
else:
  code1


#bitwise OPERATORS
arg ^ arg       #XOR


#-------
#common functions/tags:
#-------
import module1          #imports a module object for use. You can reference functions in a module object with:
module1.function1


print arg                               #prints to console
type(arg)                               #gives the type of the variable (str,int, etc.)
isinstance(arg1, variable_type1)        #returns true if the arg is of the specified varible type, false OW.
int(float)                              #gives the int value of a number - does not round.
float(int)                              #converts ints and strings to floating point numbers. for strings, '3.4' --> 3.4
str(arg)                                #converts variable into a string
input(prompt)                           #grabs keyboard input from user
abs(num)                                #returns absolute value of a number.

open('filename.txt')          #opens a file object that can be used to read the file
fileobject1.readline()        #reads characters from a file until reaching newline into a string
for string1 in fileobject1    #functions as a readline() through a loop



#-------
#METHODS:
#-------
#methods are sort of like functions, except they operate on specific objects you define. generally
object1.method1()          #runs a method on an object.
#https://teamtreehouse.com/community/difference-between-functions-and-methods-in-python


#------
#Functions:
#------
function(arg)       #parens indicate functions

#to define a function:
def function1(arg1 , arg2):
  code1

#A function ends when we get to an empty line.
#functions don't need to return arguments.
#you can use a return in a function with:
return arg1

#general functions:
raise exception1                             #raises an exception.
LookupError(optional_error_message1)         #gives an error

#------
#Loops:
#------
while condition1:
  code1

  break   #you can break out of loops with:
  #note that this breaks out of loops, but not things like "if" statements, so using break inside an if statement in a loop breaks the loop.

#for loops:
for dummy_variable1 in variable1:
  code1
#for loops will traverse through a slice storing the current value as whatever is in the dummy variable. so, if variable was a string, dummy variable would carry the value of a character of the string, and upon each iteration of the loop moves to the next variable.


#-----
#Lists
#-----
#lists are a sequence of values.
#lists are mutable, unlike strings.

var1 = ['string1','string2',1,2,3,4,['ary1','ary2']]            #initiates a list. Can also do nested lists.
emptyvar = []                                                   #this is possible
var1[0]                                                         #accesses the first element of a list.
var2 = [1,2,3]
var2[2] = 5                                                     #now var2 would look like [1,2,5]


for var1 in list1:      #var gets the value of the next list element for the loop.

range(num1)                          #range returns a list of indices from 0 to num1-1. usefule for loops, e.g.
for i in range(len(list1)):          #this will loop through list with [i] as the current index.

#Operators:
+   #concatonates Lists
*   #repeats a list x number of times    (syntax is  [1,2,3] * x )
:   #slice operator, which returns pieces of a list. Can also be used in assignment since lists are mutable.

#List methods:
list2.append('element to append')     #appends value to end of the list1
list1.extend(list2)                   #concatonates list2 onto list1. Use this to keep a copy of list2?
list1.sort()                          #arranges elements of a list from low to high.
list1.del(num1)                       #deletes the element in list1 at index position num1. [1,2,3].del(1)  would give a new list of  [1,3]. Can be used with a slice for more than one value at once.
value1 = list1.pop(num1)              #pop is like del, except pop will also return the value at the index. e.g. [1,2,3].pop(1) will return 2.
list1.remove(value1)                  #if you don't know the index but know the value, this deletes that value. returns None.

list(string1)                  #returns the characters of a string into a list.
string1.split(delimiter1)      #returns substrings seperated by delimiter1 of string1 into a list. If no argument, whitespace is used.   'my boy'.split()   returns   ['my', 'boy']
delim1.join(list1)             #returns list elements concatonated together with the delimiter into a string.


#-------------
#Dictionary
#-------------
#Mapping of values to an index of your choice.
#it's mutable
#you can use 'in', although it will on reveal keys if we're doing it directly on the dictionary.
#dictionaries using 'in' are more efficient than using 'in' with lists since it uses a hashtable.
#Dictionaries have no sort order.
#Lists and other mutable objects (like dictionaries) can't act as keys in a dictionary (although they can act as values.), because modifying a value like this will mess up the key.

dict1 = {val1: val2, val3: val4 }         #a dictionary with val1:val2 and val3:val4
dict1 = dict()                            #creates a dictionary object
dict1[val1] = val2                        #adds the mapping of val2 to index val1
dict1[val1]                               #returns the value of that index.

#funcions/methods:
len(dict1)                     #returns number of key value pairs.
dict1.values()                 #returns list of keys and values
dict1.get(val1,default1)       #returns the value corresponding to val1 if it's in the dictionary; else returns default1
sorted(dict1)                  #returns a sorted dictionary.
reversed(dict1)                #sorted, except in reverse.
dict1.items()                  #returns a sequence of tuples where each tuple is a key - value pair. This is stored in a dict_items object. Similar to other sequence of tuples. a:0, b:1, c:2 becomes a, 0   , b,1   , and c,2    in no particular order

#-----
#Tuples
#-----
#tuples are immutable sequences of values (not necessarily numbers)
#Bracket and slice operators work, along with relational operators.
#tuples can be used to swap variable values:
a, b = b, a     #this swaps the value of a with the value of b. The right side sequence (values) can be lists, strings, or tuples.
#since tuples are immutable, you can use them as keys in dictionaries.


#You can gather arguments inside a function or scatter arguments into a function with *:
def func1(*args1):          #gathers any number of arguments into a tuple for inside the function.
func(*tup1)                 #scatters a tuple into args for a function.

tup1 = val1,val2,val3,val4               #creates a tuple
tup1 = (val1, val2, val3)                #creates a tuple
tup1 = val1,                             #creates a singleton tuple

#functions/methods
tuple()                             #creates an empty tuple
tuple(val1)                         #if val1 is a sequence (string, list or tuple), we create a tuple with the subvalues in that order. 'tup' becomes 't','u','p'
divmod(num1, num2)                  #returns the tuple (num1/num2, num1%num2)
min_max(tup1)                       #returns a tuple of (minimum value of tup1, maximum value of tup1)
dict(ltup1)                         #creates a new dictionary from a list of tuples. Can also use update() to add value pairs with tuples as well.

#Zip objects:
#A zip object is a set of tuples of key value pairs, sort of:
s = 'abc'
t = 'xyz'
u = [0,1,2]
zip(s, t, u)       #would yield
(a,x,0)
(b,y,1)
(c,z,2)

zip(seq1, seq2, ...)              #returns a zip object.
list(zip1)                        #creates a list out of a zip object (a list of tuples)

for var1, var2 in tup1        #this will loop through a list of tuples, and assign var1 and var2 those tuple value pairs for use in the loop.

enumerate(seq1)                   #creates an enumerate object, which creates a sequence of pairs mapped to an index. enumerate('abc') gives 0 a, 1 b, and 2 c. We can loop over this similarly to a list of tuples.


#----------
#various functions
#---------
import random
random.randint(num1,num2)           #selects a random integer between num1 and num2, including num1 and num2
random.choic(seq1)                  #chooses an element at random from a sequence.
random.random()                     #random between 0 and 1.



#-----
#storing data (persistence)
#-----
#The os class is good for working with files and directories.
#dbm class is good for databases. Databases work similarly to dictionaries, except persistent storage?

fout = open('output.txt', 'w')               #opens a file for writing. fout here is a variable
fout.write(string1)                          #writes a string to a line. it must be a string.
fout.close()                                 #closes the file.
os.getcwd()                                  #returns current directory
os.path.abpath('memo.txt')                   #returns the absolute filepath of a file.
os.path.exists('memo.txt')                   #checks whether a file exists
os.path.isdir(path1)                         #checks whether the path or file is a directory
os.path.isfile(path1)                        #same as above, except for files.
os.listdir(dir1)                             #return a list of files and directories in dir1
db1 = dbm.open(file_name1, 'c')              #'c' will create a database if it doesn't already exist. db is the database object
db1[val1] = val2                             #a new entry in a database. val2 is stored as a bytes object, which is similar to a string.
db1.close                                    #closes the database.
pickle.dumps(val1)                           #converts most any object into a 'dump string' that can be stored in a database
pickle.loads(dumpstr1)                       #converts a dump string into the object that it used to be

file-like object1 = os.popen(os_command1)     #opens an object that behaves like an open file and executes the command passed in. You can read output with read() or readline(), if there's output. You can close the pipe like a file when complete with close().
status1 = file-like object1.close()           #status will include something if something wasn't closed right; otherwise no value is returned.
#md5sum is a UNIX command used to checksum files and see if they're identical or not.

#Modules:
#if you have a filename.py file, you can import it as a module with:
import filename            #imports your module object.
filename                   #at the prompt will return if we have a module object, at which point you can its functions with filename.function()
if __name__== '__main__'   #is often used as an if statement to skip code that isn't in __main__.

#To get around failing to open files, you can use 'try' and 'except' to quit out of the program:
try:
  fin1 - open('bad_file')
except:
  print('unable to open file')


#format operator
format_string1 % val1                  #generates a string according to what the format operator (e.g. %d) is. E.g. 'the number %d is an integer' % 42      yields the string 'the number 42 is an integer'

#format function
formatted_string = "string example {0}".format(replace)   #replaces {0} with 'replace' variable.

#-----
#classes
#-----
class class1:                 #defines a class
class1()                      #creates an object of that class (type). THis object is an instance of the class.
class1.element1 = val1        #assigns a value to an instances element.

class2 = copy.copy(class1)              #creates a copy of the class1 instance in class2.
copy.deepcopy(class1)                   #same as copy.copy(), but also copies objects that class1 refers to. E.g. box.corner is box3.corner is true when copying, but false when deep copying since corner becomes a new object.
isinstance(inst1, class1)               #checks whether inst1 is an instance of class1
type(inst1)                             #checks what the class of an instance is
hasattr(inst, attr)                     #checks whether an instance has an attribute or not.
print_attributes                        #traverses a dictionary and prints each attribute name and its corresponding value.
getattr()                               #takes an object and its attribute name and returns th attributes value

#Try can be used to find whether an object has an attribute you need as well:
try:
  x = p.x
except AttributeError:
  x = 0



#Methods and classes
#To make a function into a method, we move the function definition inside of the class definition, and then call it likewise
class1.function1()
#typically, we use functions in one of two ways, the second way being the one that's widely used:
class1.function1(object)
object1.function1()
#The name of the object the method is invoked on is called the subject. The subject is assigned to the first parameter of a method. Convention dictates we call the first parameter of a method 'self' for this reason.
class class1
  def method1(self):
    code1

__init__    #a special method invoked when an object is instantiated. You can define this as a function to put in default values or the like.
def __init__(self):
  self.element1 = default1
  self.element2 = default2
class1()    #initiates the class with this code. you can include additional parameters.
__str__     #returns a string representation of an object. You can write this up as well.
__add__     #defines the add operator for a class. There are other operators you can redefine as well.
__radd__    #right side add. This triggers when you're object is on the right side of the plus. The other will trigger if it's on either side.


#Inheritance:
#Modifying an existing class and creating a new class from it.

#To define a class2 that inherits from an existing class1, we say
class class2(class1):
  code1

#To overwrite methods from a class, simply write a new method in your new class with the same name as the method you wish to overwrite.






#python specifics:
#you can write conditional expressions in one line:
code1 if condition1 else code2            #same as:
if condition1:
  code1
else
  code2
#you can also write conditionals for bits within lines:
var1 = val1 if condition1 else val2       #will set var1 to be val2 if the condition fails.

#you can replace loops to build lists with strange in line loops, called lists comprehensions:
def somefunc(param1):
  return [var1.func2() for var1 in param1]        #will return a list of param1 passed through func2.
#Brackets indicate it's a list. Faster than equivalent loops, and often easier to read.

#generator expressions are like list comprehensions, but the generator object that's generated waits on you to generate the next value:
gen1 = (x*2 for x in range(5))
next(gen1)                           #this will give the numbers 2,4,6,8 and 10 in a generator object. The next(gen1) function gives the next result value in the sequence.
next(gen1)                           #at the end of the sequence, next() gives a StopIteration exception.
#Also can use a for loop here as well:
for val in gen1:                     #same thing as hitting next() a bunch of times.
#Often, you can use functions like sum, min, and max directly on the generator object.


any(sequence_of_boolean_values)      #returns true if there are any True boolean values in the sequence.
all(sequence_of_boolean_values)      #same as above except looks for all True


sets        #these are dictionaries with keys but no values.
set(seq1)   #this will return a set.


counter                               #like a set, but if an element appears more than once we keep track of how many times it appears (counts key reoccurances).
#counters is part of the 'collections' standard module:
from collections import Counter
Counter({'a':2, 'b' : 5})             #the result of Counter(ababbbb)
#counters return 0 if you try to access a non-existing element.


defaultdict   #also in collections.  like a dictionary, except if you access a non-existing key it can sync generation with a dictionary.


#Named Tuples:     a way to help genearte a class1
** generate keyword args
