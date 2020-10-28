# What is Data Science?
data types: working with text and data
variables: storing data 
lists: working with data in an ordered collection
dictionaries: representing data as a collection of attributes
loops and iteration: repeating a sequence of instructions 
data visualization: using plots to display data 
functions: defining and running specific procedures in code 

______________________________________________________________________________________________________

# String Methods
[instance of dataype].[method]()

str.upper() <br>

str.lower() <br>

str.title() <br>

str.endswith()  
  returns a boolean 
str.replace(x, y)
  ie. "Homer" ->> replace('o', 'O')
      returns "HOmer"
help(str)
   returns directory of str commands (exit w/ q)
str.capitalize()

string slicing:
  [2:4] = [incl, ecl]
  ie. in carrot, would return 'rr'
  [4] would return 4th char
 
concatenation:
  'xyz' + '123'
  returns 'xyz123'
  
fstring: print(f"... {} ...")

.split([separator [, maxsplit]])
  braks up str at specified separator
  returns list of stirngs
  seperator (optional): if not specified, any whitespace
  maxsplit (optional): defines max number of splits; default is -1 meaning no limit
  
.count(substring, start=..., end=...)
  searches substring and returns # of instances

.format
  complicated ***

.index(substring[, start[, end]])
  substring: to be search in str
  start/end: (optional) within str [st:end]
  returns lowed index in str where found

.isalnum()
  returns True is all char alphaneumeric
  
.isalpha()
  returns True if all char in alphabets

.is digit()

.isnumeric()

.join(iterable)
  returns str by joining all elelments of an iterable, separated by a str separator (concatenates)
  data types: list, tuple, string, dict, set
  file obj + obj defined with __iter__() or __getitem()__ method

.replace(old, new[, count])
  returns copy of str where all occuranes of a subsring are replaced by another substring
  old: substring to replace
  new: new substring to replace old
  count: (optional) number of times to replace old with new (if not specified, will replace all)
  

______________________________________________________________________________________________________

# Jupyter Notebooks
adding cell: b
deleting cell: (cmd+z) is different; escape mode + x --> z
shortcut menu: h
type code: esc mode + y
markdown: esc mode + m
shift + enter
______________________________________________________________________________________________________

# Lists
x = list(y), x = [] ->> defining a list
list[x] ->> call x index from list
indicies = range(len(list))
list(fliter9func, iterable)): returns True elements into array
accessing multpile elements: list[0:2] = list[incl:excl]

.append(item)
  item added to end of th elist
  can be any datatype
  returns None
  
.clear()
  removes all items from the list
  
.copy()
  copies old list to new list, changes to new list won't effect old list (unlike =)
  also can use slicing (new_list = list[:])
  
.count(element)
  returns # of times element is in list
  can be used with nested lists and tuples
  
.extend(iterable)
  adds all the elements of an iterable (list, tuple, string, etc) to the end of the list
  Modifies original list, does not return value
  also can append all elements to list using: + +=
  list slicing: 
    a = [1,2]; b = [3,4]
    a[len(a):] = b
    a = [1, 2, 3, 4]
  merges rather than append
  
.index(element, start, end)
  returns the index of the specified element in the list
  element: element to be searched
  start (op): start from this index
  end (op): search up to this index
  returns index of given element OR ValueEror if not found
  *only returns 1st occurane of element
  
.insert(i, elem)
  inserts element into list @ ith index
  all elements after elem shifted to right
  returns None, updates current list
  *can insert Tuples as elements
  
.pop(index)
  removes and returns an element at a given index from a list
  if index not passed, returns for (-1)
  
.remove(element)
  removes the first matching element (which is passed as an arg) from list
  throws error if element DNE
  returns None, or error
  if need to delete elements based on index, use .pop()
  
.reverse()
  reverses the elements of the list
  returns None
  can also do with slicing operator: reversed_list = list [::-1]
  accessing items in reversed order: for x in reversed(list):
.sort(key=..., reverse=...)
  key (op): func that serves as key for he sort comparison
  reverse (op): if True, sorted list is sorted in descending order
  changes original list
  no rreturn
  to return sorted list (with original unchanged) use sorted()
  ie. list.sort(key = len, reverse = true/false)
      OR sorted(list, key=len)
  
______________________________________________________________________________________________________

# Dictionaries
func(arg, arg)['name']

.clear()
  removes all items from dict
.copy()
  returns shallow copy of dict
  doesn't change original dict (unlike =)
.fromkeys(sequence[, value])
  creates new dict from given sequence of elements with value provided by user
  sequence: sequence of elements which is to be used as keys for new dict
  value (op): value which is set to each element of dict
.get(key[, value])
  returns value for specific key, if key is in dict
  key: key to be searched in dict
  value (op): value to be returned if key is not found; defaults to None
.items()
  returns a view object that displays a list of dict key, value tuple pairs
  
______________________________________________________________________________________________________

# Variables

______________________________________________________________________________________________________

# Scalar Types
ints, floats, bools, str, None, complex, bytes
scalar type: holds a single value (vs. collection type, which holds many values and can be changed w/p id value change -> ie. not being destroyed and remade)
  scalar types in python are immutable, they are detroyed and remade everytime the value is reassigned
int
  can represent a value that is countable
  are only positive or negative whole numbers
  discrete values
  int(x) to cast an int or round a float
  indexing with square brackets requires int
float
  decimal numbers
  measurments, result of division, or calculations involving other floats
  continuous values
  float() to cast as float
  underfloq
    can occur when attempting to calculate a number smaller than what can be stored in memory
    ints are stored differently than floats
      ints are direct representation of binary form
    **dont really understand this
    can cause issues with relaly small numbers
 boolean
  True or False
  1 or 0
  full or empty values
  binary in nature
  not negates bool
  result of <, >, >=, <=, == is always boolean
string
  collection of characters
  concatenation +
  str() to cast
None
  describes the absence of a value
  functions auto return None if no return statement or empty return statement
  None can be used as a placeholder
  can sub for a n/a data (missing data)
 
______________________________________________________________________________________________________

# Numpy
numpy arrays
  CAN ONLY INCLUDE A SINGLE DATA TYPE
  when + doesnt concatenate, adds each instance to its respecive pair
  ie. [1,2,3] + [1,2,3] = [2,4,6]
  np.array()
  ie. np_height_in = np.array(height_in)
  can multiply, etc each entry by an operator
  ie. np_height_m = np.array(height_in) * 0.0254
      bmi = np_weight_kg/(np_height_m**2)
  can create array of bools and subset it within another array, and itll only return the values that match the True values
  ie. light = np.array(bmi<21). #creates bool array of true false for those that are <21
      print(bmi[light])         #subsets in bmi array to only return bmis that fit the True values
  can also subset like normal lists
  ** subsetting ([xyz])
  ie. array([100:111]) returns enteries from index 100 to 110 inclusive
  
2D numpy arrays
  .shape => returns (rows, cols); not a method, is an attribute
  array[0][2] == array[0,2]
  calling just cols or rows is easy -> array[r:c] with slicing telling python to include all
  ie. np_baseball[:,1] select just the 2nd column
      print(np_baseball[123,0]) print the 124th player's height
  Can create an array of conversions by row/col and multiply
    ie. array with 3 cols, new array with conversion factors in 3 cols, multiply to convert whole array

basic statistics
  np.mean(array[:,0])
  np.median(array[:])
  np.corrcoef(array1, array2). see if 2 array rows/cols are correlaed
  np.std(array) std dev
  np.sum()
  np.sort()
  Very fast calculations because all 1 data type
  
  ______________________________________________________________________________________________________
  
# Numbers and Booleans
= += -= *= /= **=
+ - * / // **
// floor division
% remainder (mod)
== finds relation between two booleans, relational operator
!= result type: boool; "not equal to"
< <= > >=
and, or ->> bool op used to preform logical conjuction
not: returns True when op is false orr 0, vice versa
del: removes item/element at a specified index location from lis, not returned; takes index as arg, deletes itema at index
int: # w/o decimal, +/-
float: # with decimale, +/- (always returned by /)
True: bool(1)
False: 0, None, len() ie. [] or " ", bool(0)

# Basic Operators
// floor division
  if either is a float, will return a float
% modulus
  trial division: see if divides in evenly, common step to find primes and all divisors of given num
  parity: mod 2, whether an integer is even or odd  
  if either is a float, will return a float
Order of op
  PEMDAS, M includes %
  if same precedence, left to right
Logical ops
  and, or, !
  btwise: & = and, |. = or, ~ = not
    exclusive or (^) = only when 1 op is true (vs or where bith can be true
  not evaluated 1st, then and, or last
  bitwise 1st, then logical op
  excl or befor or
comparison ops
  < > <= >= == !=

  ______________________________________________________________________________________________________

# Control Flow
if (any expression that resolves as either True or False) --> condition
else ==> under all other conditions

#test
