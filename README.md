# What is Data Science?
data types: working with text and data<br>
variables: storing data <br>
lists: working with data in an ordered collection<br>
dictionaries: representing data as a collection of attributes<br>
loops and iteration: repeating a sequence of instructions <br>
data visualization: using plots to display data <br>
functions: defining and running specific procedures in code <br>

______________________________________________________________________________________________________

# String Methods
[instance of dataype].[method]()

str.upper() <br>

str.lower() <br>

str.title() <br>

str.endswith()  <br>
  returns a boolean <br>
str.replace(x, y)<br>
  ie. "Homer" ->> replace('o', 'O')<br>
      returns "HOmer"<br>
      
help(str)<br>
   returns directory of str commands (exit w/ q)<br>
str.capitalize()<br>

string slicing:<br>
  [2:4] = [incl, ecl]<br>
  ie. in carrot, would return 'rr'<br>
  [4] would return 4th char<br>
 
concatenation:<br>
  'xyz' + '123'<br>
  returns 'xyz123'<br>
  
fstring: print(f"... {} ...")

.split([separator [, maxsplit]])<br>
  braks up str at specified separator<br>
  returns list of stirngs<br>
  seperator (optional): if not specified, any whitespace<br>
  maxsplit (optional): defines max number of splits; default is -1 meaning no limit<br>
  
.count(substring, start=..., end=...)<br>
  searches substring and returns # of instances

.format<br>
  complicated ***

.index(substring[, start[, end]])<br>
  substring: to be search in str<br>
  start/end: (optional) within str [st:end]<br>
  returns lowed index in str where found<br>

.isalnum()<br>
  returns True is all char alphaneumeric<br>
  
.isalpha()<br>
  returns True if all char in alphabets<br>

.is digit()

.isnumeric()

.join(iterable)<br>
  returns str by joining all elelments of an iterable, separated by a str separator<br> (concatenates)<br>
  data types: list, tuple, string, dict, set<br>
  file obj + obj defined with __iter__() or __getitem()__ method<br>

.replace(old, new[, count])<br>
  returns copy of str where all occuranes of a subsring are replaced by another substring<br>
  old: substring to replace<br>
  new: new substring to replace old<br>
  count: (optional) number of times to replace old with new (if not specified, will replace all)<br>
  

______________________________________________________________________________________________________

# Jupyter Notebooks
adding cell: b<br>
deleting cell: (cmd+z) is different; escape mode + x --> z<br>
shortcut menu: h<br>
type code: esc mode + y<br>
markdown: esc mode + m<br>
shift + enter<br>
______________________________________________________________________________________________________

# Lists
x = list(y), x = [] ->> defining a list<br>
list[x] ->> call x index from list<br>
indicies = range(len(list))<br>
list(fliter9func, iterable)): returns True elements into array<br>
accessing multpile elements: list[0:2] = list[incl:excl]<br>

.append(item)<br>
  item added to end of th elist<br>
  can be any datatype<br>
  returns None
  
.clear()<br>
  removes all items from the list<br>
  
.copy()<br>
  copies old list to new list, changes to new list won't effect old list (unlike =)<br>
  also can use slicing (new_list = list[:])
  
.count(element)<br>
  returns # of times element is in list<br>
  can be used with nested lists and tuples
  
.extend(iterable)<br>
  adds all the elements of an iterable (list, tuple, string, etc) to the end of the list<br>
  Modifies original list, does not return value<br>
  also can append all elements to list using: + +=<br>
  list slicing: <br>
    a = [1,2]; b = [3,4]<br>
    a[len(a):] = b<br>
    a = [1, 2, 3, 4]<br>
  merges rather than append<br>
  
.index(element, start, end)<br>
  returns the index of the specified element in the list<br>
  element: element to be searched<br>
  start (op): start from this index<br>
  end (op): search up to this index<br>
  returns index of given element OR ValueEror if not found<br>
  *only returns 1st occurane of element
  
.insert(i, elem)<br>
  inserts element into list @ ith index<br>
  all elements after elem shifted to right<br>
  returns None, updates current list<br>
  *can insert Tuples as elements
  
.pop(index)<br>
  removes and returns an element at a given index from a list<br>
  if index not passed, returns for (-1)
  
.remove(element)<br>
  removes the first matching element (which is passed as an arg) from list<br>
  throws error if element DNE<br>
  returns None, or error<br>
  if need to delete elements based on index, use .pop()
  
.reverse()<br>
  reverses the elements of the list<br>
  returns None<br>
  can also do with slicing operator: reversed_list = list [::-1]<br>
  accessing items in reversed order: for x in reversed(list):<br>
  
.sort(key=..., reverse=...)<br>
  key (op): func that serves as key for he sort comparison<br>
  reverse (op): if True, sorted list is sorted in descending order<br>
  changes original list<br>
  no return<br>
  to return sorted list (with original unchanged) use sorted()<br>
  ie. list.sort(key = len, reverse = true/false)<br>
      OR sorted(list, key=len)<br>
  
______________________________________________________________________________________________________

# Dictionaries
func(arg, arg)['name']

.clear()<br>
  removes all items from dict
  
.copy()<br>
  returns shallow copy of dict<br>
  doesn't change original dict (unlike =)
  
.fromkeys(sequence[, value])<br>
  creates new dict from given sequence of elements with value provided by user<br>
  sequence: sequence of elements which is to be used as keys for new dict<br>
  value (op): value which is set to each element of dict<br>
  
.get(key[, value])<br>
  returns value for specific key, if key is in dict<br>
  key: key to be searched in dict<br>
  value (op): value to be returned if key is not found; defaults to None<br>
  
.items()<br>
  returns a view object that displays a list of dict key, value tuple pairs
  
______________________________________________________________________________________________________

# Variables

______________________________________________________________________________________________________

# Scalar Types
ints, floats, bools, str, None, complex, bytes<br>
scalar type: holds a single value (vs. collection type, which holds many values and can be changed w/p id value change -> ie. not being destroyed and remade)<br>
  scalar types in python are immutable, they are detroyed and remade everytime the value is reassigned<br>
  
int<br>
  can represent a value that is countable<br>
  are only positive or negative whole numbers<br>
  discrete values<br>
  int(x) to cast an int or round a float<br>
  indexing with square brackets requires int<br>
  
float<br>
  decimal numbers<br>
  measurments, result of division, or calculations involving other floats<br>
  continuous values<br>
  float() to cast as float<br>
  underfloq<br>
    can occur when attempting to calculate a number smaller than what can be stored in memory<br>
    ints are stored differently than floats<br>
      ints are direct representation of binary form<br>
    **dont really understand this<br>
    can cause issues with relaly small numbers<br>
    
 boolean<br>
  True or False<br>
  1 or 0<br>
  full or empty values<br>
  binary in nature<br>
  not negates bool<br>
  result of <, >, >=, <=, == is always boolean<br>
  
string<br>
  collection of characters<br>
  concatenation +<br>
  str() to cast<br>
  
None<br>
  describes the absence of a value<br>
  functions auto return None if no return statement or empty return statement<br>
  None can be used as a placeholder<br>
  can sub for a n/a data (missing data)<br>
 
______________________________________________________________________________________________________

# Numpy
numpy arrays<br>
  CAN ONLY INCLUDE A SINGLE DATA TYPE<br>
  when + doesnt concatenate, adds each instance to its respecive pair<br>
  ie. [1,2,3] + [1,2,3] = [2,4,6]<br>
  np.array()<br>
  ie. np_height_in = np.array(height_in)<br>
  can multiply, etc each entry by an operator<br>
  ie. np_height_m = np.array(height_in) * 0.0254<br>
      bmi = np_weight_kg/(np_height_m**2)<br>
  can create array of bools and subset it within another array, and itll only return the values that match the True values<br>
  ie. light = np.array(bmi<21). #creates bool array of true false for those that are <21<br>
      print(bmi[light])         #subsets in bmi array to only return bmis that fit the True values<br>
  can also subset like normal lists<br>
  ** subsetting ([xyz])<br>
  ie. array([100:111]) returns enteries from index 100 to 110 inclusive<br>
  
2D numpy arrays<br>
  .shape => returns (rows, cols); not a method, is an attribute<br>
  array[0][2] == array[0,2]<br>
  calling just cols or rows is easy -> array[r:c] with slicing telling python to include all<br>
  ie. np_baseball[:,1] select just the 2nd column<br>
      print(np_baseball[123,0]) print the 124th player's height<br>
  Can create an array of conversions by row/col and multiply<br>
    ie. array with 3 cols, new array with conversion factors in 3 cols, multiply to convert whole array<br>

basic statistics<br>
  np.mean(array[:,0])<br>
  np.median(array[:])<br>
  np.corrcoef(array1, array2). see if 2 array rows/cols are correlaed<br>
  np.std(array) std dev<br>
  np.sum()<br>
  np.sort()<br>
  Very fast calculations because all 1 data type<br>
  
  ______________________________________________________________________________________________________
  
# Numbers and Booleans
= += -= *= /= **=<br>
+ - * / // **<br>
// floor division<br>
% remainder (mod)<br>
== finds relation between two booleans, relational operator<br>
!= result type: boool; "not equal to"<br>
< <= > >=<br>
and, or ->> bool op used to preform logical conjuction<br>
not: returns True when op is false orr 0, vice versa<br>
del: removes item/element at a specified index location from lis, not returned; takes index as arg, deletes itema at index<br>
int: # w/o decimal, +/-<br>
float: # with decimal, +/- (always returned by /)<br>
True: bool(1)<br>
False: 0, None, len() ie. [] or " ", bool(0)<br>

# Basic Operators
// floor division<br>
  if either is a float, will return a float<br>

% modulus<br>
  trial division: see if divides in evenly, common step to find primes and all divisors of 

given num<br>
  parity: mod 2, whether an integer is even or odd  <br>
  if either is a float, will return a float<br>
  
Order of op<br>
  PEMDAS, M includes %<br>
  if same precedence, left to right<br>
  
Logical ops<br>
  and, or, !<br>
  btwise: & = and, |. = or, ~ = not<br>
    exclusive or (^) = only when 1 op is true (vs or where bith can be true<br>
  not evaluated 1st, then and, or last<br>
  bitwise 1st, then logical op<br>
  excl or befor or<br>
  
comparison ops<br>
  < > <= >= == !=

  ______________________________________________________________________________________________________

# Control Flow
if (any expression that resolves as either True or False) --> condition<br>
else ==> under all other conditions<br>


  ______________________________________________________________________________________________________

# List Basics
A list is a collection of arbitrary objects, often called an array in other programming languages. The contents of a list can be thought of as ordered, in that a list guarantees that its contents are numerically indexed. The items, or elements of a list can be accessed by the numeric index. In Python, a list is mutable in the sense that its contents can be rearranged, replaced, or deleted. A list can be nested to arbitrary depth. The list datatype is the primary construct on which you will perform iteration, or going item-by-item across a data structure.<br>

creating a list:
  some_list = []
  some_list = [x,y,z]
  some_list = list()
  some_list = list(some_other_collection)

concatenating lists:
  can concatenate lists with '+' operator

''' python
first_list = ['This', 'is', 'list', '1']
second_list = ['add', 'me', 'to', 'list', '1']

concatenated_list = first_list + second_list

# This will print ['This', 'is', 'list', '1', 'add', 'me', 'to', 'list', '1']
print(concatenated_list)
'''