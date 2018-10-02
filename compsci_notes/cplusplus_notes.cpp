

/*
C++ notes:
every line in C++ ends in a semicolon
we must have the function int main() somewhere. main returning 0 means success by convention, whereas any positive int is failure.
l-value vs r-value: L values are associated with a persistent memory address, r-values are not. Basically, r-values are actual number/characters, where l-values are variables that store that value.
initializing variables just allocates the memory there, and doesn't write over the value that exists there presently. So initalizing the variable will have the variable set with a garbage value.
you can initialize functions as well as variables, apparently, which makes sense.


Comments:
//comment
/*multiline comment
*/

//Libraries:

#include <libary>     //includes that library. <> these carrots are actually necessary here.
#include <iostream>   //cin and cout

/*
Anything that can be declared, whether it be a variable, or constant, function, method, or even class: all are identifiers.

remember, aliasing is basically having two things point to the same physical object.

std - this namespace contains basically everything standard c++ uses, i.e. types, functions, you name it.
*/


//--------------------
//Basic commands:
//--------------------
return var;      //returns a variable.
return int ();   //the parens here are necessary; without parens we'd just be referencing a type.

/*
fundamental types:
http:   //www.cplusplus.com/doc/tutorial/variables/ - this has a full list.
char, int		some integer. chars are for characters, generally.
float, double
void		has no value. like null, i guess?
decltype(nullptr)		null pointer, why in gods name.
boolean		either true or false
wchar_t		wide character

strings are denoted with double quotes, whereas individual characters are denoted with single quotes.

types can be modified with: signed or unsigned, and short or long.
*/
typedef <type> <var>;   //defines a typedef, which is an alias for a type. <var> is the name of the alias, and <type> is the type to be aliased.
using <var> = <type>;   //works equivalently.


//initialize variables:
type var,var,var;   //this is possible.
type var = value;   //these are all equivalent.
type var (value);
type var {value};

auto var = value;      //this assigns var the type of the value automatically. Should be used for only assigning variables to other variables, probably.
decltype(var1) var2;   //gives var2 the type of var1.


//compound types:
//Strings:
string var = string_var;   //declares a string object. Not a string literal.
string var = "hello"       //"hello" is a string literal, so I think var in this case will be a string literal.
var = "text /
text"                      //strings can be concatonated by just putting a whitespace between two strings: e.g. "abc" "efg".


//-----------
//constants
//------------
/*
any value is a constant, basically. like "1" or "\n" are both literals. there can be string literals.
constants are of a certain assigned type:
e.g. 1 is a int, 1.0 is a float, and 75u is an unsigned int. Use modifiers like these to set types of constants.

nullptr is the literal for a null pointer.
*/
const name = constant value;   //this will give an alias to the constant.

//you can also replace things in preprocessing before the program is compiled:
#define name = const;   //basically, all of this is 


//------------
//operators
//------------
/*
+*-/%       obvious arithmatical operators.

compound assignment
+=,-=,*=,/=,%=,<<=,>>=,&=,^=,|=
*/


//increment with ++ or --
y = ++x   //means that y gets whatever ++x is. Increment x first.
y = x++   //means that y gets whatever x is, and then we increment x. pretty nuts.

/*
comparison operators:
==, !=, >, <, >=, <=

Logical operators:
!,&&,||

conditional ternary operator:
condition ? val1:val2		returns val1 if condition is true, val2 otherwise.

comma operator:
used to handle mutliple expressions where only 1 is expected.


bitwise operators:
& and
| inclusive or
^ exclusive or
~ bit inversion (unary complement)
<< shifts bits left
>> shifts bits right.

typecasting:
var = type (val)			value of val is typecast into var as type. e.g. converting floating points to integers.

sizeof(typename_or_variablename)				returns the number of bytes a type or variable uses.
http:   //www.cplusplus.com/doc/tutorial/operators/    - operator precedence table

*/
//-----------------
//Program flow:
//-----------------
if (condition) {statements}   //single statements can be input without braces (insofar as they get their semicolons)
else if () {}
else {}

while () {}
do {} while ();                          //this executes the statement first, and then continues executing the statements
for (statement;condition;statement) {}   //for loops can be run with whichever of these arguments we want. Generally, 1st is initialization, and 3rd is increment, but I don't think it matters.
for ( declaration:range ) {}             //decleration might be "char c", where range is some collection. variable declared in decleration gets all of the values in the collection during the loop.

break;         //breaks out of a loop
continue;      //breaks out of loop but continues executing
goto label1;   //goto
label1:        //syntax for labels for use by goto

switch (expression) {   //switch
	case value1:
		//statements
		//statements
	case value2:
		//statements
}

//--------
//Functions
//--------
type function_name(type var, type& var, const type& var, type var=val) {   //type indicates what type of variable a function will return (e.g. int). Use void to indicate that a function need not return anything (doesn't need keyword, even)
//code //must include "return" if returning something, void otherwise.
}
//const keeps whatever variable we push in from getting altered

//vars here are parameters of the function.
//the & after type means that we pass in the variable by reference, not just the value, so modifying the variable will actually change the thing.

//efficiency: passing variables by reference is more efficient, since we don't need to make copies of the values. To lock referenced variable values so they can't be changed:
type function(const type& var)

//Inline functions:
inline type functionname(){}   //when the compiler runs, this will physically place the code at this point in the function, instead of having to reference it elsewhere. most compilers do this automatically.

//Declaring a function before defining it:
//functions normally can't be called until they are defined (remeber python?). If you declare a function, you can call the function before you define it in the code. Useful for 1) organization, or 2) mutually dependent functions.


//Overloading functions: if two functions have different number of parameters/different param types, we will automatically use the function that corresponds to the function inputs.
//if you want to build two functions that have different parameters but the same body (e.g. summing integers is less intensive that floats, but it happens the same way), we do this with "template"


//TEMPLATES
template <class sometype1,sometype2>
template <typename sometype1,sometype2>          //this is equivalent to the above line. The typename keyword here can be a substitute for class. Which might be the way to go.
type function(sometype1 var1,sometype2 var2){}   //Sometype is basically used as a keyword/holder for the real type. type can be replaced by a set type, or even sometype.

//Call a function like this like so:
b = functionname<int,double> (param,param);   //this uses int as the sometype here. C++ also has automatic parameter detection:
b = functionname(param,param)

//non-templates args
template <class T, int N>   //fixed type here, meaning type is set at compile time. Also for similar reasons, you can only pass constants into the type here (since we build the function at compile time)
void function(T var){
return var*N
}

function<int,9>(10)   //You'd call it like on the left; the function accepts one parameter, but templated with the type our parameter is along with passing in the constant that we have available.

//--------
//Scope
//--------
//Global scope - just declare variables outside of any function. global scope variables have memory allocated for them at the start (and also have vales set to 0); local variables don't, and just have value at the memory location.
//Block (local) scope - declare a variable inside a function.
//apperently, anything inside any "block" is considered local to that block, a block being anything inside braces. so


func a{
	int x = 4
	int y = 5
	{
		int x = 5     //this is valid, and is only 5 inside this block.
		cout << y+x   //this prints 10
	}
}


//Namespace:
//a namespace is a declarative region that gives a scope to identifiers within it. I.e. variables, functions,methods, classes etc. in this all have the specific scope
namespace <namespace name>{     //opens up a namespace
	<identifier>;                  //declares variable inside of name.
	
}
namespace::identifier           //you can access a specific identifier in a namespace like this

//namespaces can be "split":
namespace first {identifier1}
namespace second {identifier2}
namespace first {identifier3}   //"first" now has identifier1 and identifier3.

namespace new_name = namespace_1;   //creates a new alias for namespace_1

//Using
using namespace <namespace_name>;                     //this means we will be using the namespace for the rest of the block. if used globally (outside of any block), they will be used for all of the file unless another is specified.
using <name_space_name>::<identifier_in_namespace>;   //this means whenever the identifier is referenced in the remainder of the block, we will use the identifier in the namespace.


//--------
//Arrays
//--------
type var [number_of_elements] = {val1,val2};   //intializes an array. first part declares the array, second part is if we want to assign values.
int ary [5] = {1,2};                           //initializes an array with 5 elements. this means that the array will look like [1,2,0,0,0] - if we decide to assign values, we actually start assigning values instead of just pointing to memory.
int ary [5] {1,2};                             //same as above statement; assignment is automatic.
int ary [] = {1,2,3,4}                         //c++ will autmatically decide the size of ary.
ary[index]                                     //references this array value.
int ary [5][3]                                 //declares a multidimensional array.

//you can't define an array (e.g. with {}) after it's been declared, although you can set individual elements of it.

//passing arrays into functions:
void func (int ary[])          //allows you to pass an array into a function. this just passes the pointer of where the array's block of memory starts, so you'd need to pass in size?
void func (int ary[][5][10])   //passes a multidimensional array into a function. since we don't know the size of the memory block, we need to explicitly state it here.

//library array:
//basically allows you to reference a whole block of memory, at the expense of being an expensive operation.

//you'll need
#include <array>
array<int,3> myarray = {1,2,3}
myarray.size()   //example function


//Char arrays:
char ary[20]      //declares a 20 character long array.
//in order to say when we are done putting characters in an array, we have the character '\0'. Strings automatically have this appended to the ends of their arrays.
//the difference between these arrays and strings is that strings have dynamic memory, where we allocate the memory for arrays based on their size. You can use this to limit string size.
mysting.c_str()   //returns the array that the string would be.

//--------
//Pointers
//--------
&var       //the pointer of var.
*pointer   //accesses the value stored at the pointer.

type * pointer1       //declares "pointer" that points to data with a type of "type"
type * p1, * p2, v3   //declares p1 and p2 as pointers, but v3 is just a variable of "type"

void functionname (type& var)   //this means we only accept pointers with type 'type' as variables.
//apparently, this actually passes the variable pointer even when calling the variable. i.e., you'd call it like "functionname(var)", not "functionname(&var)"

//Arrays:
//arrays are basically a pointer with a certain amount of memory, so setting a pointer from an array will drop you at the first address in that array:
var ary[40]
var * p_ary = ary[40]   //this is a valid operation, and p_ary equals the address at ary[0]. 
++p_ary                 //p_ary equals the address at ary[1] now. So for any typical pointer case, array[5] == *(pointer_to_array+5)
//works for string literals as well

//++pointer will not go to the next immediate memory address, but the next immediate address for a something of that type. since long is bigger than int, steps between pointers to long will be bigger.

//Constants:
int * const p = &var         //this creates a constant pointer
const int *p = &var          //this creates a pointer for a constant
int const * p = &var         //confusingly, this is the same as above. Note position of *.
const int * const p = &var   //this creates a constant pointer for a constant


//Pointers pointing to pointers
char a = 5
char *b = &a
char **c = &b   //c points to where the pointer is stored in memory.

//void pointer:
void * pointer   //declares a pointer to a void type. Must be typed before being dereferenced. useful for passing generic pointers into functions:
func(void *pointer, string pointer_type) {
	if pointer_type == "int"{
		int * typed_pointer = (int*) pointer
	}
	}               //if we have a pointer, we can create a pointer with an actual type based off of that pointer.

//null pointer:
int * p = nullptr;   //creates a pointer that actually doesn't point to an address. cannot be dereferenced

//function pointer:
int (*function_ptr)(param,param) = old_function_name   //creates a pointer for the old function. in this case int is the return type of the function


//--------
//Dynamic Memory
//--------
pointer = new type;       //allocates memory for the pointer during runtime. This means that type can change. Exceptions get thrown if we run out of memory.
pointer = new type [5];   //allocates memory for an array of the pointer during runtime. This means that 5 can be a variable as well.
//if we can't allocate enough memory, we will return a nullptr. for user input, we probably should throw an error for this.

type obj;
pointer = &obj;       //when we declare obj in scope, we delete obj when we're done; i.e. the local variable won't persist.
pointer = new type;   //this method allows us to allocate memory for an object and have it persist after the local scope variable might be deleted (we'd just return the pointer).

delete pointer   //frees memory that is allocated to a pointer during runtime. now pointer is a nullptr
delete[] pointer

//--------
//Data Structure (struct is also name of a public class)
//--------
struct struct_name {                //holds a bunch of data. structures are types, so anything can happen with these that happen with normal types; e.g. pointers, arrays.
int a
float b
struct_2 c                          //struct_2 is just another structure instanced here.
} obj_name,obj_name,obj_array[5];   //creates objects that use this structure. Also can create an array of those objects.

struct_name obj_name;
obj_name.a = 6   //sets a value for the obj_name.a

struct_name * pointer = &obj_name;
(*pointer).a   //this references whatever is in obj_name.a
pointer->a     //equivalent to above line - uses the arrow operator
*pointer.a     //something else entirely; tries to reference *(pointer.a), which I guess is pretty bogus 99% of the time.


//union
union union_name {   //like a struct in form, but each member uses the same address in memory, so you can't keep more than one thing in a union at a time.
int a
float b
} union_obj;

//unions as members of a class or structure can be declared with no name, and we will assume the union when referencing one of its members:
class classname{
union union_name{int a;};
union {int b};
}
classname::a   //this should reference the a in the union. b could be referenced similarly


//enums
enum <type_name> {<name1>,<name2>,<name3>} <enum_objs>;		the enum type - assigning variables with values will actually assign them an index in the array. e.g. var1 = name3; gives var1 a value of 2
enum <type_name> {<name1>=1, <name2>};   //normally we start at 0 and add 1 for each, but this will start at 1 and work upwards.
enum color {red,green} mycolor;
mycolor = green;
if mycolor == red {}                     //this is valid based on the previous lines
//no idea how enum classes work, or why you'd ever use them.

//--------
//Classes
//--------
//classes can be declared with class or struct (and also unions, which still can only hold one member at a time, along with functions).
//by default, class keyword declares a class with private members, whereas struct defaults public members.
class class_name
struct class_name

class class_name {
		//anything in here is private, meaning you can't get to it unless you're an actual member or "friend" of the class
		//protected means that you can access it if you are a child of a class in addition to being a member of the class.
public:      //anything underneath this is public; else private. THESE are important, even in inherited classes.
}obj_name;   //way to declare object

class_name obj_name;   //another way to declare an object

obj_name.a   //accesses identifier a of obj_name

int classname::functionname () {return 5}   //declaring a new function as part of classname. The :: is the scope operator, which tells you where you're doing something.

//Constructor:
class classname{
 classname () {}                   //a constructor; we just declare it while we're building the class here.
}
classname::classname (params) {}   //a constructor after we build a class. this is a function with a special name that automatically executes upon creating a new class object. Note how constructors CAN'T return values.
classname objname (params);        //this is a constructor in action
classname objname {params};        //works same as above; potentially less confusing since it won't look like you're calling a function
classname objname = param;         //works if class only has one param.
//constructors can only be called implicitly when an object is created, never again afterwards by that object.
//constructors can be overloaded the same way other functions can.

classname::classname objname (int x,int y) : a(x), b(y) {remaining code}   //this will initialize a constructor that automatically set value a to x.
classname::classname objname (int x,int y) : a{x}, b{y} {}                 //same as above, except using braces instead.

//pointers:
classname * pclassname   //this declares a pointer to the type of classname.


//Overloading operators:
classname operator + (const classname& param);              //declares the function as a function on classname.
classname classname::operator+ (const classname& param){}   //here, param is a obj of classname. What we've done is defined a function operator+ which takes one argument, and 
obj1 + obj2                                                 //this calls the overloaded operator, if obj1 and obj2 have the operator overloaded.
obj1.operator+(obj2)                                        //equivalent to the above statement.


//this:
//'this' is a pointer to the object of the method being executed. So if we have an obj.func() we're running and 'this' is inside of it, 'this' is equivalent to the obj pointer.


//static:
static int n;    //example of static member. A static class member is shared for all objects of a class. static members must be declared outside of a class:
classname::n=0   //setting a static class member ousie of a class.
//functions can also be static, but they can't reference dynamic class members inside of the function.


//const member functions:
//idea here is to have some sort of class wherein we can't edit the members.
const classname obj;                 //declares a constant class object. these can't have modifications made to them. you can still use a constructor on them to initialize them, but they are for the most part read only.
int functionname() const {}          //if this function is declared inside a constant class, we're allowed to call this function from outside the class.
//these const classes are useful if you are passing a class into a function by reference:
void func(const classname& var) {}   //if we need to have a function not alter a class, having something like this passes the object in as a constant.
//you can overload a function to have both const and non-const versions - the const version will get called iff the object is considered a const.


//Class templates:
//works the same way as templates except we pass the 'type' into a class instead of a function.
//if we define a class function outside of a class and this has a return type of 'T' (a template), it must be declared as follows:
template <class T>                  //must include this line, for some reason.
T classname<T>::functionname() {}   //the second T on this line specifies that the function's template parameter is the same as the class template parameter (something to do with having to call class T twice, I assume).

//template specialization:
template <class T> class classname {}   //generic template for all types.
template <> class classname <char> {}   //this means if we reference a class and construct it with a char, we will use this instead of the generic class. there isn't inheritance between this and the other class, FYI, so this acts as more of an overload than anything else.

//--------
//Special Class members
//--------
//default constructor: a constructor with no arguments that is assumed by the compiler if you don't write your own constructor. If you DO write a constructor, the compiler will no longer make this for you, so you'll need to build an override for the constructor
classname () {}   //example of a default constructor being declared in classname

//destructor: called when a class is getting deleted to free up dynamically allocated memory. Doesn't return anything and takes no arguments. Called when the program ends.
~classname () {}   //example of a destructor. Note how we don't return anything and take no arguments.

//copy constructor:
//a constructor for shallow copies of a class is created by the compiler implicitly. Shallow copies copy the members of a class, which won't work for pointers, as duplicate objects will be accessing the same memory
classname (const classname&) {};            //declares a copy constructor. generally, you can copy the constructor, but then replace calls to a variable with calls to the pointer of that variable.
classname (const classname& x) {x.member}   //generally, something like this can be used for a copy constructor to reference the member of the object.
classname obj1 = obj2                       //example of when a copy constructor would be used.

//copy assignment:
//like copy constructor, but called when an object already has been initialized. like the copy constructor, the compiler implicitly builds one which builds a shallow copy, which is a problem for pointers (again)
classname& operator= (const classname&)   //overloads operator=. need to do things like delete/reuse pointers here.

//move constructor and assignment:
//for unnamed objects, this takes the unnamed object and "moves it" to the class we're creating.
classname obj = classname()   //example of when move gets used; we're constructing a class based off of the classname().

MyClass (MyClass&& x) : ptr(x.ptr) {x.ptr=nullptr;};   //declares a move constructor. the code on this line also 1) grabs the x pointer and assigns it, and 2) deletes the former x.ptr.
MyClass& operator= (MyClass&& x){                      //declares a move assignment. notice the &&. since this is an unnamed object, basically reassigning the pointer for class members will work for this:
	delete ptr; 
    ptr = x.ptr;
    x.ptr=nullptr;
    return *this;
}                                                      //example code for move assignment.
//compilers already optimize many of these cases, e.g. when we get a return value from a function. This makes a lot of sense, seeing as how these functions seem to just shift some pointers around.

//implicit members:
//there are implicit functions generated for each of these cases. You can specify whether they should be generated or not (and probably should) like so:
function_declaration = default;   //explicitly compiles the default function
function_declaration = delete;    //explicitly prevents the default function from compiling

//--------
//Friendship
//--------
//friendship is not transitive.

class classname {
	friend classname friendname(const classname&)   //declares friendname as a friend of classname, so now we can access members of classname with friendname even though friendname is not a member of classname.
	friend class friendclassname                    //friend class declaration.
	}
classname friendname(const classname&) {}        //we declare friendname as a function with a return type of classname. This ISN'T a member of classname.

//--------
//Inheritance
//--------
class derivedclassname : public parentclassname   //declares a class as a derived class of the parent class. "public" can also be "private" or "protected".
//public: derived classes inherit every base class member except: constructors and destructor, assignment operator members, friends, and private members. constructors and destructors aren't inherited, but they are autmatically called from the base class by the derived class.

//constructors:
class parentclass {}
class childclass {
	childclass() : parentclass () {}                  //this code makes the childclass constructor overload the parent class constructor.
	childclass(int a, int b) : parentclass (a,b) {}   //this does the same, except with parameters.
}

//there is such a thing as multiple inheritance:
class classname : protected parentclass1, public parentclass2   //multiple inheritance

//------------
//Polymorphism
//------------
//pointers to a derived class is type compatible with pointers to the base class. HOWEVER, pointers here can't access members of the derived class; only members of the base class.
//a virtual function skirts around this; pointers can access derived class functions if the function is declared as a virtual function in the parent class.
class parent{
	virtual int functionname() {return 1};                  //now pointers to the "child" class will be able to call functionname().
	void anotherfunction() {cout << this->functionname()}   //this function returns the contents of a virtual function with this; this way we don't have to build "anotherfunction" in all of the derived classes.
} objparent;
class child : public parent {
	int functionname() {return 5} //
} objchild;
child * pchild = &objchild;
cout << pchild -> functionname();
parent * pparent = &objparent;
cout << pparent -> functionname();                       //this will print the value assigned in the virtual function, since the pointer is to the parent class.

//Abstract base classes: a class with at least one pure virtual function.
//Interface: an abstract class with no non-virtual functions. This means that the class has to be 1) public, and 2) serves just as a hub for different functions you write. No real concept of interfaces in C++, but there are in other langauges.
//--------
//type conversions (typecasting)
//--------
short b = 2000
int a
a = b        //2000 is now and int, no explicit type conversion required. this is called an IMPLICIT CONVERSION.
bool c = a   //c is true; 0 is false, all other values are true. for pts, it's false only if it's a nulptr.
//floats to ints just truncates the value.

//classes:
//implicit conversions are handled by classes with an assignment operator, a single-argument constructor, or a typecast operator.
class classname1 {}
class classname2 {
operator classname1() {return classname1()};   //example of a typcast operator - we define an operator and we're essentially told what to do. This is for nigh identical classes. Since the return type should always be the destination type, we don't need to specify it here.
}

//Explicit conversions: there can be problems when a function takes in an argument - it might automatically convert it with an implicit conversion, something we might want to avoid.
//functions and constructors can be marked as explicit to fix this:
class A {
explicit A () {}                 //ensures the contructor for classname must explicitly be that type. can't call this constructor with sytax classname obj1 = obj2; must be classname obj1 (obj2)
} objA;
void functionname(A paramname)   //builds function as normal.
class B {} objB;
functionname(objA);              //this works
functionname(objB);              //this doesn't, since objB does not fulfill the explicit constructor of class A.

//type casting:
int (x)   //converts x to an int. You can, unfortunately, convert pointers from one type to another this way, which really messes things up. there is special handling for all of this stuff

dynamic_cast <typename> (expression)                               //can only be used with pointers and references to classes. can upcast and downcast with this (upcast meaning convert pointerofderived to pointerofbase, and downcast meaning vice-versa)
base_class * pointertoderived_obj = new derived_class;
base_class * pointertobase_obj = new base_class
new_pointer = dynamic_cast <derivedtype*> (pointertoderived_obj)   //this works
new_pointer = dynamic_cast <derivedtype*> (pointerofbase_obj)      //this'll return a null pointer, because we're trying to convert a base object which is inherently not as complete as the derived object (since derived will have at least 1 more member)

static_cast <typename> (expression)                            //upcasts and downcasts for pointers to related classes. unlike dynamic casts, no full object checks are performed. So the statement above would work with staticcast, but could cause problems.
new_pointer = static_cast <derivedtype*> (pointerofbase_obj)   //this works.
//this also has other things it can do, which are...numerous. generally allows a great degree of freedom to the programmer.

reinterperet_cast   //can convert pointers to any other pointer, regardless of class. dangerous and crazy.
const_cast          //casts a value as a constant. useful.

typeID:
#include <typeinfo>   //must include to use typeid
typeid (expression)   //returns the type of the expression, whether that be a class or int or whatever. seems super useful. types pointers as well.

//------
//Exceptions
//------
try {
	throw 20          //throws exception
}                  //"try" block. runs code and possibly throws an exception
catch (int e) {}   //catches the exception if the exception is of type int. Generally, you can look up the exceptions thrown for the functions you're using (e.g. stoi (string to integer) and invalid_argument).
catch (...) {}     //catches the exception of any type (won't run if we already caught something).

//exception specification: used in old code.
#include <exception>                  //library that gives us the base class "exception"
class classname: public exception {   //exception is the name of the base class "exception", which can be overwritten.  the function what() is a virtual member function of the base class, so you can overwrite this to create your own custom messages.
	const char* what() const throw(){    //returns a pointer to a char? array. This needs the const throw() call. not totally sure what it's for, but probably necessary due to returning a const.
		return "n and p should be non-negative";
    }
}myexception;                         //you'd declare an object, then when the exception is thrown we can reference myexception.what().

catch(&exception e) {       //catches the exception, by the address
	cout << e.what() <<endl;   //this prints the what message
}

//assert
assert(condition);    //if the condition fails, then we throw an exception for that assertion.
//when writing tests for other functions, you'll basically have to come up with examples to test. Randomness probably means a lot of work/writing the functions yourself.
//--------
//preprocessor directives
//--------
#include <iostream>   //example of a preprocessor directive, as indicated by the # symbol.

#define identifier replacement      //#define - used to replace identifier with replacement throughout the code.
#define GRAVITY 9.8                 //would replace GRAVITY in the code with 9.8.
#undef GRAVITY                      //tells the code to quit replacing things. needs to be done before multiple #define macros.
#define f(x) #x                     //a single # will replace the expression between the parens with a string literal of the line. the function f is just how we're demnstrating this here. now:
cout << f(this will be a string);   //yields "this will be a string" as the string literal.
#define glue(a,b) a ## b            //concatonates a and b:
glue(co,ut) << "cout is now what's on the left"

//conditionals:
#ifdef GRAVITY    //only works if GRAVITY has been defined previously.
int a = GRAVITY
#endif            //ends the "if" section
#ifndef GRAVITY   //opposite of ifdef; only works if GRAVITY is NOT defined.

#if GRAVITY < 9.8   //your typical if statement sequence.
#elif etc           //note how we use else if for code, but elif here.
#else
#endif

//line control:
#line number filename       //redefines where we show the error is coming from. Number is the line number, and filename is the filename. Setting this does mess up the error message for the rest of the file, though.
#error "my error message"   //generates an error message.

#include <library>
#include "file"   //what this sounds like.

#pragma   //? specific to the compiler.

//there are some predefined macros that you can use. These start and end with two underscores, e.g,:
__DATE__
__TIME__
cout << __LINE__   //current line being compiled
__FILE__           //filename of the source being compiled.

//--------
//Input/Output
//--------
/*
A stream is an entity where the program can insert or extract characters to/from. basically a "string" object.

Stream:
cin - strandard input stream
cout - standard output stream
cerr - strandard error stream
clog - standard logging output stream.
*/

//most programs have cout defaulted to the screen.
// << is the insertion operator
cout << "Output sentence"         //gives the string to the stream, which then prints to screen if that's where that is pointing. You can chain <<, so
cout << "output " << "sentence"   //gives "output sentence" to the screen.
//use "string/n" to print a newline with the string, or cout << "string" << endl;  endl will create a newline and flush the streams buffer, which is another way of saying output is requested to be physically written to the device. Affects fully buffered streams, which c++ is generally not. this operation has some overhead.

//>> is the extraction operator
int age;
cin >> age;   //grabs age from cin. Generally cin waits for a user to enter input from the keyboard which is complete when they hit 'enter'
//To request multiple data, we can use cin >> input1 >> input2;
//cin considers whitespace to terminate the value being extracted, so strings must be single words. to get an entir line, use getline (cin, mystring);


while(getline(cin,string_var)) {}   //to loop over lines of input until we run out:


stringstream(string_var)   //allows a string to be treated as a stream. can be used to convert strings into ints, or ints into strings, or any other type from/to strings, for that matter.


//functions:
getline(cin >> ws, <string>);   //extracts a whole line of input. ws extracts as many whitespaces as possible, stopping when we find non-whitespace, and discards the whitespace.
//note that we here might need to preface this with cin.ignore() - if we use cin before this, chances are /n (newline) is buffered, so getline will quit immediately.

cout << fixed << setprecision(1) << 100.12345 << endl;   //fixed allows us to show a set number of decimal places after a number. setprecision() sets how many decimal places we'll need. in this case, we'd just print 100.1

//numbers
printf("%.2f", <num>)   //returns up to two decimal places of a float.

//----------
//IO with files
//----------
ofstream objname;   //stream to write TO files. ofstream is the name of the class
ifstream            //stream to read FROM files
fstream             //both reading and writing to files.

//these are derived classes of istream and ostream. cin and cout are derived classes of them as well.
//member functions:
open(filename, mode)   //filename is the filepath, whereas mode can decide how we're opening the file (input, output, binary, etc.) Flags can be combined with "|". ofstream, ifstream, and fstream are just variations on the default file modes.
ios::binary            //this flag opens a file in binary mode, meaning it ignore file extensions and straightup reads the file for us.
is_open();             //returns true if the filestream is open, false OW.
close();               //closes the file

getline(filename,line)   //this is a reference to the stream object itself (i.e. the file if we performed "open()" on it.) (need not be preceded by "objname."). line is here a string that will take on the value of the next line in the file.

//stateflags:
bad()     //returns true if a reading or writing operation fails.
fail()    //returns true if bad() or if there is a formatting error, e.g. alpha character is extracted when trying to read an int number.
eof()     //returns true when we've reached the end of the file.
good()    //returns true if the other functions haven't returned true.
clear()   //resets state flags.

//stream positioning:
tellg()   //returns where the "get" position in the stream is right now. Returns type "streampos", which acts as an int for the most part, except you may not be able to do operations with it and other ints, just other streampos?
tellp()   //returns "put" position

seekg(position)            //tells us where to put the get position.
seekp(offset, direction)   //same, except put. These functions are both overloaded. Here direction is a flag: ios:beg, ios:cur, ios:end for beginning, curent position, and eof respectively. offset is a positive number, i think, of type "streamoff"

//Binary files:
//don't need to use getline(), since data is not formatted into lines necessarily.
//functions:
read(memory_block,size)   //memory_block is of type char* (pointer to char), and size is a number of chars we're expecting (in an array).
write(memory_block,size)


//---------
//Iterators
//---------
classname<int> obj1;                                                            //declares object, <int> is for template reasons?
classname<int>::iterator iteratorname;                                          //declares an iterator.
for (iteratorname = obj1.begin();iteratorname != obj1.end();iteratorname++) {   //we set iterator to being, then quit on end, and increment. loops through the iterator.
		cout << iteratorname                                                          //the iterator here will print the pointer - an iterator is a pointer
		cout << *iteratorname                                                         //this will print the value at the pointer.
}
//in the case that we want to use a template for this instead of an already defined type, we'll need to use typename so the compiler knows we'll have a type there when it runs:
typename classname<T>::iterator iteratorname;
int i = distance(obj1.begin(),obj1.end())                                       //calculates number of elements between the two.

//---------------
//typename
//---------------
//qualified names are names that specify a scope; e.g. std::cout is a qualified name, while cout is not.
//dependent names are names that are not known at the point of instantiation, whereas dependent names are. typedefs can transfer this quality.
template <class T>
T t;               //t here is dependent
int i;             //i here is non-dependent.
typedef T t_var;   //t_var is dependent, since T creates dependent names.

//qualified, dependent names require a typename declaration in front of them. See the code in section "Iterators".

//---------
//REGEX CLASS NOTES
//---------
regex regex_var(".*")                                  //initializes a regex var. .* is the example here.
std::smatch match_var;                                 //declares results match variable.
if (regex_search(searchee,match_var,regex_var)) {      //the function here returns true if our searchee string matches somewhere with regex_var. match_var gets matching groups stuffed in there:
	string_var = match_var(1);                            //returns the matching group out of the regex_var expression.
}
regex_replace(searchee,regex_var,replacer_with_this)   //if we find regex in the search string, we replace whatevers in it with the replacer_with_this.
replacer = "$1"                                        //this will directly reference (dependingon the number) a "/1" or "/2" etc. group in something like regex_replace.

//---------
//specific functions and tools:
//---------
round(float_var)                                         //takes a float and returns the value rounded to the nearest whole number.
stoi(string_var)                                         //converts a string to an integer.
swap(T& a, T& b)                                         //where T is a template. This swaps two values. swap(x,y) means x gets y's value, and vice versa. Can overload this if this sort of swapping ain't efficient enough.
accumulate(iterate_begin,iterate_end,init)               //note that init here will be the type that accumulate returns, so you must type it before hand for special cases (note that on it's page, it has "class T")
cout << fixed << setprecision(1) << 100.12345 << endl;   //setprecision sets the number of decimal places printed.

//--------
//OTHER NOTES ABOUT SPECIFIC BUILT IN CLASSES
//--------
#include <list> //list is a dynamic list where you can insert members anywhere in the list. http:   //en.cppreference.com/w/cpp/container/list
#include <queue>                        //queue, for queue structure. has pop and push, but need to grab return value seperately.
#include <sstream>                      //stringstreams.
istringstream stream_var(string_var);   //declares a new stringstream object, which behaves like a stream (i or o or just stringstream for i/o).
vector<int> var_name;                   //declares a vector - this is an array that can change size.
list<int> var_name; //

map<type1,type2> mapvar;      //like a dictionary. associates type1 as key with type2 as value. uses pairs:
pair<type1,type2> var_name;   //pair of values. type1 is first, and type2 is second.
set<>                         //this is an ordered set of elements with unique values.
unordered_set <>