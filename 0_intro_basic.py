"""
Print
--------------------------------------------------------------------------
Used to print information to the console
"""
# This is a comment
print('HELLO WORLD')

"""
Advanced printing
--------------------------------------------------------------------------
By using f-strings or format strings we can get full control of printing
"""
print("The number {} is {:.4f}".format('pi', 3.14159265359))
# or similar with f-string:
print(f"The number {'pi'} is {3.14159265359:.3f}")


"""
Variables
--------------------------------------------------------------------------
Important built-in variable types in python.
The type function can be used to determine the type
"""

my_sincerity = True
my_number = 5
my_rational = 3.14
my_string = 'abc'
my_list = [2, 4, -2, 5]
my_tuple = (7, 'horse')
my_dict = {'yes': 25, 'no': 12}
print('type(my_sincerity)', type(my_sincerity))
print('type(my_number)   ', type(my_number))
print('type(my_rational) ', type(my_rational))
print('type(my_string)   ', type(my_string))
print('type(my_list)     ', type(my_list))
print('type(my_tuple)    ', type(my_tuple))
print('type(my_dict)     ', type(my_dict))

print('is my_number an int', isinstance(my_number, int))
print('is my_number a str ', isinstance(my_number, str))
print('is my_list an int  ', isinstance(my_list, int))
print('is my_list a list  ', isinstance(my_list, list))

"""
Strings
--------------------------------------------------------------------------
Strings are sequences of characters.
"""

my_string_single = 'This is a string'
print('is my_string_single a str: ', isinstance(my_string_single, str))

# If you need to use the single quote (the apostrophe) in your string,
# you may use the double quote:
my_string_double = "This is a string with '"
print('is my_string_double a str: ', isinstance(my_string_double, str))

"""
Lists
--------------------------------------------------------------------------
An ordered collection of python objects.
Lists can be be subset using index
"""
# List
# How do we index in python?
asimplelist = [2, 4, -2, 5]
acomplicatedlist = [2, 'text', [100, 200]]


print('One element:          ', asimplelist[0])
print('Another element:      ', asimplelist[1])
print('2nd lists 2nd element:', acomplicatedlist[1])
print('2nd lists 3rd element:', acomplicatedlist[2])


print('Entire list: ', asimplelist)
n = 1
m = 3
print('Two elements:', asimplelist[n:m])


print('Preceding elements: ', asimplelist[:m])
print('Succeeding elements:', asimplelist[n:])
print('All elements:       ', asimplelist[:])


"""
Changing list
--------------------------------------------------------------------------
List can be changed using different built in functions
"""

asimplelist = [10, 4, -2, 5]
print(asimplelist)

asimplelist[0] = 2
print(asimplelist)

asimplelist.append(8)
print(asimplelist)

asimplelist.pop(2)
# Gives the list:
print(asimplelist)

asimplelist.pop(-1)
print(asimplelist)

"""
List comprehension
--------------------------------------------------------------------------
Build a new lists by running through and existing list.
(related to for loops which we will get back to)
"""

my_list = [2, 4, -2, 5]
new_list = [2*elem for elem in my_list]
print(new_list)

positive_list = [elem for elem in my_list if elem > 0]
print(positive_list)
    
# or even more advanced
somelist = ['3', 1, None, 'six', '0', 5]
intlist = [int(el) for el in somelist if isinstance(el, str) and el.isdigit() or isinstance(el, int)]
print(intlist)

# Also note the difference between:
list_1 = my_list * 2
list_2 = [2*elem for elem in my_list]
print(list_1)
print(list_2)
"""
Tuples
--------------------------------------------------------------------------
The elements of tuples are accessed like the elements of lists,
but the elements of tuples cannot be changed (immutable).
"""

simple_tuple = (1, 2)

"""
Dictionaries
--------------------------------------------------------------------------
Dictionaries are unsorted collections of Python objects indexed by keywords.
A dictionary has curly brackets, { and }, around key-value pairs that are
separated by commas. The key and the value in a pair are separated by a :.
"""
mydict = {'dogs': 5,
          'cats': 2,
          'rats': 0} 
# A dictionary may be extended like this:
mydict['mice'] = 8
# and queried like this:
how_many_mice = mydict['mice']
how_many_birds = mydict.get('birds', 0)

# Key-value pairs can be looped over using:
mydict = {'dogs': 5, 'cats': 2, 'rats': 0}
for key, value in mydict.items():
    print(key, value)


"""
Loops
--------------------------------------------------------------------------
for-loops runs through values of an iterable objects.
usefull when you want to do the same thing multiple times.
"""

# Lets multiply some numbers eith 2:
print(2*2)
print(4*2)
print((-2)*2)
print(5*2)

# if this should be done many times we could instead use:
for elem in [2, 4, -2, 5]:
    print(elem*2)

# This is similar to the List comprehension we saw earlier
    
# lets look at something slightly more advanced:
total_length_of_strings = 0
for elem in ['zero', 'one', 'two', 'three']:
    total_length_of_strings += len(elem)
    print('string: {:7s} has length: {:3d}'.format(elem, len(elem)))
print('total length of strings:    ', total_length_of_strings)

"""
lambda functions
--------------------------------------------------------------------------
also known as anonymous functions, are small, restricted functions.
"""

adder = lambda x, y: x+y
print('adder(0,1)', adder(0, 1))
print('adder(0,2)', adder(0, 2))
print('adder(1,2)', adder(1, 2))

"""
function
--------------------------------------------------------------------------
More elaborate defenitions of functions. Some are already build in:
print, type, isinstance, etc.
But we can also define our own
(the ",end=' = '" changes the new line in the print function)
"""

def my_func(arg1, arg2):
    print('my_func({},{})'.format(arg1, arg2), end=' = ')
    var1 = min(10, arg1)
    var2 = min(10, arg2)
    res = var1 * var2
    return res
print(my_func(5,7))
print(my_func(5, 12))
print(my_func(15, 12))


"""
function - default values
--------------------------------------------------------------------------
A function can be defined with default values for the arguments.
"""
def my_sum(x=5, y=7, z=11):
    res = x + y + z
    print('x={} y={} z={} res={}'.format(x, y, z, res))
    return x + y + z


my_sum(1, 2, 3)
my_sum(1, 2)
my_sum(1)
my_sum()

# or values can be given in another order:
my_sum(z=0, y=2)

"""
Boolean expressions
--------------------------------------------------------------------------
A variable of the Boolean type may only take two values, either True or False.
boolean comparison operators. Examples are >, <, <=, etc.
"""

0 == 0, 0 <= 5 - 5, 'three' == 'Three'.lower()

0 == 1, 3 == 3 - 6, 3 == 'three'

# membership operator: in
'a' in 'char', 3 in (1, 2), 3 in [2, 3], 3 in {2: 'two', 3: 'three'}

# Boolean expression may be combined with and and or:
expr1 = 1 == 1 and 1 > 2
expr2 = 1 == 1 or 1 > 2
expr1, expr2

# and negated with not:
not True, not(True), not(False), not(1==2), 1 not in [0, 2, 4]

"""
Branching (if-elif-else)
--------------------------------------------------------------------------
A variable of the Boolean type may only take two values, either True or False.
boolean comparison operators. Examples are >, <, <=, etc.
"""

yourstring = input('Write a number \n')
if yourstring == '0':
    res = 'zero'
elif yourstring.isdigit():
    res = 'positive'
elif yourstring[0] == '-' and yourstring[1:].isdigit():
    res = 'negative'
else:
    res = 'not a number'
print('Your input {} is {}'.format(yourstring, res))



