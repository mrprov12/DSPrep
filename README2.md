* [What is Data Science?](#s1)
      * [data types:](#s1-0-1)
      * [variables:](#s1-0-2)
      * [lists:](#s1-0-3)
      * [dictionaries:](#s1-0-4)
      * [loops and iteration:](#s1-0-5)
      * [data visualization:](#s1-0-6)
      * [functions:](#s1-0-7)
      * [to find all methods for a data type:](#s1-0-8)
* [String Methods](#s2)
      * [Strings are sequences](#s2-0-1)
      * [declaring a string](#s2-0-2)
      * [repetition](#s2-0-3)
      * [containment](#s2-0-4)
      * [[instance of dataype].[method]()](#s2-0-5)
* [Jupyter Notebooks](#s3)
* [Lists](#s4)
* [Dictionaries](#s5)
      * [consist of key/value pairs ](#s5-0-1)
      * [Example from question 3 on adding key value pairs from learn](#s5-0-2)
      * [accessing dict values](#s8-0-1)
* [the second argument to enumerate starts counting i at 1](#s9)
* [find the 13th letter](#s10)
* [this will error](#s11)
      * [dict as accumulators](#s11-0-1)
      * [creating a word count dictionary example from learn](#s12-0-1)
      * [func(arg, arg)['name']](#s13-0-1)
* [Variables](#s14)
* [Scalar Types](#s15)
      * [scalar type:](#s15-0-1)
      * [int](#s15-0-2)
      * [float](#s15-0-3)
      * [boolean](#s15-0-4)
      * [string](#s15-0-5)
      * [None](#s15-0-6)
* [Numpy](#s16)
      * [numpy arrays](#s16-0-1)
      * [2D numpy arrays](#s16-0-2)
      * [basic statistics](#s16-0-3)
* [Numbers and Booleans](#s17)
* [Basic Operators](#s18)
      * [// floor division](#s18-0-1)
      * [% modulus](#s18-0-2)
      * [given num](#s18-0-3)
      * [Order of op](#s18-0-4)
      * [Logical ops](#s18-0-5)
      * [comparison ops](#s18-0-6)
* [Control Flow](#s19)
* [GitHub Commands Terminal](#s20)
* [List Basics](#s21)
      * [LISTS ARE MUTABLE](#s21-0-1)
      * [creating a list:](#s21-0-2)
      * [calling an elem from a list:](#s21-0-3)
      * [changing elem in list at index:](#s21-0-4)
      * [concatenating lists:](#s21-0-5)
      * [list memembership:](#s21-0-6)
      * [list slicing:](#s21-0-7)
      * [nested lists:](#s21-0-8)
      * [unpacking a list:](#s21-0-9)
      * [functions and methods](#s21-0-10)
* [accumulators:](#s22)
      * [examples:](#s22-0-1)
* [nt:](#s23)
* [loat:](#s24)
* [ool flags:](#s25)
* [ist](#s26)
* [lattened nested lists](#s27)
* [arallell lists:   ](#s28)
* [iteration with for loops](#s29)
* [break, continue, pass](#s30)
      * [break out of for loop:](#s30-0-1)
* [this for loop will exit after 50](#s31)
* [reak out of while loop](#s32)
      * [continue for skipping loops:](#s32-0-1)
      * [pass:](#s32-0-2)
* [while loops](#s33)
* [define a counter](#s34)
* [notice that setting x to 2 will allow entrance into the while](#s35)
* [put the counter in the `while` to avoid an infinite loop](#s36)
      * [while loop using conditional check:](#s36-0-1)
      * [open-ended problems:](#s36-0-2)
* [Make the index of counts correspond with the](#s37)
* [number of trials](#s38)
* [Make a simple terminal graphic to display the distribution](#s39)
* [ of number of trials needed to achieve a value](#s40)
* [ below a given threshold.](#s41)
      * [for or while?](#s41-0-1)

______________________________________________________________________________________________________


# <a id='s1' />What is Data Science?
### <a id='s1-0-1' />data types:
 working with text and data<br>
### <a id='s1-0-2' />variables:
 storing data <br>
### <a id='s1-0-3' />lists:
 working with data in an ordered collection<br>
### <a id='s1-0-4' />dictionaries:
 representing data as a collection of attributes<br>
### <a id='s1-0-5' />loops and iteration:
 repeating a sequence of instructions <br>
### <a id='s1-0-6' />data visualization:
 using plots to display data <br>
### <a id='s1-0-7' />functions:
 defining and running specific procedures in code <br>

### <a id='s1-0-8' />to find all methods for a data type:
  print(dir(datatype))

#### <a id='s' />isinstance(elem, type)
  returns bool True if same type
  returns bool False if different type

#### <a id='s' />type(elem)
  returns <class type>
______________________________________________________________________________________________________

# <a id='s2' />String Methods
### <a id='s2-0-1' />Strings are sequences
    Recall from earlier that strings are a sequence type in Python, but they are also immutable. This means they can be iterated through and sliced, for example, but do not support indexed reassignment or the del statement.

### <a id='s2-0-2' />declaring a string
  string = ''
  string = ""
  casting  -- > str(element_to_be_cast)

### <a id='s2-0-3' />repetition
  string*num repeats string num number of times

### <a id='s2-0-4' />containment
  "p" in "python"
    returns True

### <a id='s2-0-5' />[instance of dataype].[method]()

#### <a id='s' />str.upper() 

#### <a id='s' />str.lower() 

#### <a id='s' />str.title() 
 
#### <a id='s' />str.endswith()  
  returns a boolean <br>

#### <a id='s' />str.replace(x, y)
  ie. "Homer" ->> replace('o', 'O')<br>
      returns "HOmer"<br>
      
#### <a id='s' />help(str)
   returns directory of str commands (exit w/ q)<br>

#### <a id='s' />str.capitalize()

#### <a id='s' />string slicing:
  [2:4] = [incl, ecl]<br>
  ie. in carrot, would return 'rr'<br>
  [4] would return 4th char<br>
 
#### <a id='s' />concatenation:
  'xyz' + '123'<br>
  returns 'xyz123'<br>
  
#### <a id='s' />fstring: print(f"... {} ...")

#### <a id='s' />.split([separator [, maxsplit]])
  braks up str at specified separator<br>
  returns list of stirngs<br>
  seperator (optional): if not specified, any whitespace<br>
  maxsplit (optional): defines max number of splits; default is -1 meaning no limit<br>
  
#### <a id='s' />.count(substring, start=..., end=...)
  searches substring and returns # of instances

#### <a id='s' />.format
  "single_and_escaped = 'I won\'t use anything other than single quotes!"

#### <a id='s' />.isspace()
  checks if character is a whitespace char liek ' ', '\t', '\n', '\r' etc

#### <a id='s' />.index(substring[, start[, end]])
  substring: to be search in str<br>
  start/end: (optional) within str [st:end]<br>
  returns lowed index in str where found<br>

#### <a id='s' />.isalnum()
  returns True is all char alphaneumeric<br>
  
#### <a id='s' />.isalpha()
  returns True if all char in alphabets<br>

#### <a id='s' />.is digit()

#### <a id='s' />.isnumeric()

#### <a id='s' />.join(iterable)
  "".join(lst)

  returns str by joining all elelments of an iterable, separated by a str separator<br> (concatenates)<br>
  data types: list, tuple, string, dict, set<br>
  file obj + obj defined with __iter__() or __getitem()__ method<br>

#### <a id='s' />.replace(old, new[, count])
  returns copy of str where all occuranes of a subsring are replaced by another substring<br>
  old: substring to replace<br>
  new: new substring to replace old<br>
  count: (optional) number of times to replace old with new (if not specified, will replace all)<br>
  

______________________________________________________________________________________________________

# <a id='s3' />Jupyter Notebooks
adding cell: b<br>
deleting cell: (cmd+z) is different; escape mode + x --> z<br>
shortcut menu: h<br>
type code: esc mode + y<br>
markdown: esc mode + m<br>
shift + enter<br>
______________________________________________________________________________________________________

# <a id='s4' />Lists
x = list(y), x = [] ->> defining a list<br>
list[x] ->> call x index from list<br>
indicies = range(len(list))<br>
list(fliter9func, iterable)): returns True elements into array<br>
accessing multpile elements: list[0:2] = list[incl:excl]<br>

#### <a id='s' />.append(item)
  item added to end of th elist<br>
  can be any datatype<br>
  returns None
  
#### <a id='s' />.clear()
  removes all items from the list<br>
  
#### <a id='s' />.copy()
  copies old list to new list, changes to new list won't effect old list (unlike =)<br>
  also can use slicing (new_list = list[:])
  
#### <a id='s' />.count(element)
  returns # of times element is in list<br>
  can be used with nested lists and tuples
  
#### <a id='s' />.extend(iterable)
  adds all the elements of an iterable (list, tuple, string, etc) to the end of the list<br>
  Modifies original list, does not return value<br>
  also can append all elements to list using: + +=<br>
  list slicing: <br>
    a = [1,2]; b = [3,4]<br>
    a[len(a):] = b<br>
    a = [1, 2, 3, 4]<br>
  merges rather than append<br>
  
#### <a id='s' />.index(element, start, end)
  returns the index of the specified element in the list<br>
  element: element to be searched<br>
  start (op): start from this index<br>
  end (op): search up to this index<br>
  returns index of given element OR ValueEror if not found<br>
  *only returns 1st occurane of element
  
#### <a id='s' />.insert(i, elem)
  inserts element into list @ ith index<br>
  all elements after elem shifted to right<br>
  returns None, updates current list<br>
  *can insert Tuples as elements
  
#### <a id='s' />.pop(index)
  removes and returns an element at a given index from a list<br>
  if index not passed, returns for (-1)
  
#### <a id='s' />.remove(element)
  removes the first matching element (which is passed as an arg) from list<br>
  throws error if element DNE<br>
  returns None, or error<br>
  if need to delete elements based on index, use .pop()
  
#### <a id='s' />.reverse()
  reverses the elements of the list<br>
  returns None<br>
  can also do with slicing operator: reversed_list = list [::-1]<br>
  accessing items in reversed order: for x in reversed(list):<br>
  
#### <a id='s' />.sort(key=..., reverse=...)
  key (op): func that serves as key for he sort comparison<br>
  reverse (op): if True, sorted list is sorted in descending order<br>
  changes original list<br>
  no return<br>
  to return sorted list (with original unchanged) use sorted()<br>
  ie. list.sort(key = len, reverse = true/false)<br>
      OR sorted(list, key=len)<br>
  
______________________________________________________________________________________________________

# <a id='s5' />Dictionaries
### <a id='s5-0-1' />consist of key/value pairs 
  d = { 
    "key" : "value",
     "key2" : "valu2",
      etc
      }

  d = dict()

  keys must be an immutable type (int, float, string, tuple, etc)

  keys must be unique, only one occurance per dict

  value type can be any, including objects defined by the user

  dictionaries make good containers for analyzing data

  dicts are NOT ORDERED, non-ordinal

#### <a id='s' />general example:
  ```python
  some_dict = {
             key1: value1,
             key2: value2,
             key3: value3
             }

```

#### <a id='s' />specific example:
```python
a_dict = {
          'hello': 1234,
          3: tuple([1,2,3,4]),
          4.716: ['a', 'b', 'c', 'd'],
          True: {1:'a', 2:'b', 3:'c'},
          (1,2,3,4):'hey'
         }

print(a_dict)
```

#### <a id='s' />specific example 2:
```python
item1, price1 = 'salt', 2.31
item2, price2 = 'butter', 3.23
item3, price3 = 'flour', 5.67
item4, price4 = 'baking soda', 3.20
item5, price5 = 'sugar', 3.50

baking_dict = {
               item1: price1,
               item2: price2,
               item3: price3,
               item4: price4,
               item5: price5,
      }

print(baking_dict)
```
### <a id='s5-0-2' />Example from question 3 on adding key value pairs from learn
```python
''' Write a function called letter_idx and will track the indices of where the vowels occur in a string. This function should:

Take a word or a sentence as an argument
Return a dictionary with keys representing the vowels that occur in that sentence, and values representing the indices where that vowel occurs in the word or sentence
For this exercise the letter y is considered a vowel
For example:

letter_idx("Hello there!") ---> {'e' : [1, 8, 10], 'o' : [4]}'''

#solution <a id='s6' />1:
def letter_idx(s):
    vowels_and_indicies = {}
    
    for char in(s):
        if char in "aeiouyAEIOUY":
            vow_ind = []
            for i, c in enumerate(s):
                if c == char:
                    vow_ind.append(i)
            vowels_and_indicies[char] = vow_ind
                    
                    
    return vowels_and_indicies

<a id='s7' />#solution2:
def letter_idx(word):
    # This is the vowel index accumulator
    vowel_dict = {}

    # Use 'enumerate' since both index and character are used
    # Use 'word.lower()' since the function should be case-insensitive
    for idx, char in enumerate(word.lower()):
        if char in "aeiouy":
            # If the vowel is already in the dictionary, append the index
            if char in vowel_dict:
                vowel_dict[char].append(idx)
            # Otherwise, initialize the dictionary key with a new list containing the index
            else:
                vowel_dict[char] = [idx]

    return vowel_dict

<a id='s8' />#solution3
def letter_idx(word):
    vowel_dict = {}

    for idx, char in enumerate(word.lower()):
        if char in "aeiouy":
            vowel_dict[char] = vowel_dict.get(char, []) + [idx]

    return vowel_dict

    '''The dict.get(key, init) method will return the value in a dictionary corresponding to key if the key is present in the dictionary, otherwise the init value will be returned. This allows you to set the default value to the empty list [], and then concatenate [idx]. Note: if init is not specified, the default value will be None.'''

```

### <a id='s8-0-1' />accessing dict values
can access key/values using the following with iteration:
```python
    for key, val in d.items()
```

#### <a id='s' />example 2:

``` python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
d = {}

# <a id='s9' />the second argument to enumerate starts counting i at 1
for i, letter in enumerate(alphabet, 1):
    d[i] = letter

# <a id='s10' />find the 13th letter
thirteenth = d[13]

print(thirteenth)
```

note: check for membership before attempting to access a dict key to avoid throwing errors:

``` python
d = {'dog':'cat', 'frog':'gnat'}

# <a id='s11' />this will error
if 'snake' in d:
    print(d['snake'])
else:
    print('there is no snake in here')
```

### <a id='s11-0-1' />dict as accumulators

``` python
#As <a id='s12' />with the other built-in data types in python, the dict type can be used as an accumulator. Consider the function below that unpacks a list of tuples into a dict accumulator.

def return_dict_of_tuples(list_of_tups):
    d = {}

    for tup in list_of_tups:
        d[tup[0]] = tup[1]

    return d


list_of_tups = [('ford', 20),
('chevy', 30), ('toyota', 40), ('volkswagen', 50)]

print(return_dict_of_tuples(list_of_tups))
```

### <a id='s12-0-1' />creating a word count dictionary example from learn

```python
rand_paragraph = '''"New York City member-supported radio station WFUV named Free Yourself Up its New Dig, aka Album of the Week. On the album, the band "strives to empower and liberate in an age of turmoil," says FUV. "It’s a confident collection of songs that reflects the quartet’s nearly decade-and-a-half of music making. (cite nonsuch records announcement New York City member-supported radio station WFUV named Free Yourself Up its New Dig, aka Album of the Week. On the album, the band "strives to empower and liberate in an age of turmoil," says FUV. "It’s a confident collection of songs that reflects the quartet’s nearly decade-and-a-half of music making."'''

def get_clean_word_list(paragraph):
    to_remove = ['"', '(', ')', '.']
    cleaned = paragraph[:]
    for punc in to_remove:
        cleaned = cleaned.replace(punc, '')
    cleaned = cleaned.lower()
    return cleaned.split(' ')


def word_count_dict(paragraph):
    word_list = get_clean_word_list(paragraph)

    # clean up double quotes, lowercase
    for i, word in enumerate(word_list):
        word_list[i] = word.lower()

    word_count_dict = {} # dict()

    for word in word_list:
        if word not in word_count_dict.keys():
            word_count_dict[word] = 0
        word_count_dict[word] += 1

    return word_count_dict

# <a id='s13' />Here you use .items() to traverse the dict you've made
for word, count in word_count_dict(rand_paragraph).items():
    print(f'{word}: {count}')
```


### <a id='s13-0-1' />func(arg, arg)['name']

#### <a id='s' />.clear()
  removes all items from dict
  
#### <a id='s' />.copy()
  returns shallow copy of dict<br>
  doesn't change original dict (unlike =)
  
#### <a id='s' />.fromkeys(sequence[, value])
  creates new dict from given sequence of elements with value provided by user<br>
  sequence: sequence of elements which is to be used as keys for new dict<br>
  value (op): value which is set to each element of dict<br>
  
#### <a id='s' />.get(key[, value])
  returns value for specific key, if key is in dict<br>
  key: key to be searched in dict<br>
  value (op): value to be returned if key is not found; defaults to None<br>
  
#### <a id='s' />.items()
  returns a view object that displays a list of dict key, value tuple pairs<br>
  can use to get a list of tuples for key/value pairs in a dict
``` python
              fruit_dict = {'apple': 20, 'peach':15, 'pineapple':3}

              tup_list = list(fruit_dict.items())

              print(tup_list)
```

#### <a id='s' />.keys()
  returns list of keys

#### <a id='s' />.values()
  returns list of values

``` python
      fruit_dict = {'apple': 20, 'peach':15, 'pineapple':3}

      keys_list = fruit_dict.keys()
      print(keys_list)

      values_list = fruit_dict.values()
      print(values_list)
```

#### <a id='s' />.pop('some_key'[, default])
  'some_key' = key which is to be searched for removal<br>
  default = value which is to be returned when key is not in dict<br>
  returns: 
      If key is found - removed/popped element from the dictionary<br>
      If key is not found - value specified as the second argument (default)<br>
      If key is not found and default argument is not specified - KeyError exception is raised<br>


#### <a id='s' />del d['some_key']
  deletes key/value pair at 'some_key'
______________________________________________________________________________________________________

# <a id='s14' />Variables

______________________________________________________________________________________________________

# <a id='s15' />Scalar Types
ints, floats, bools, str, None, complex, bytes<br>
### <a id='s15-0-1' />scalar type:
 holds a single value (vs. collection type, which holds many values and can be changed w/p id value change -> ie. not being destroyed and remade)<br>
  scalar types in python are immutable, they are detroyed and remade everytime the value is reassigned<br>
  
### <a id='s15-0-2' />int
  can represent a value that is countable<br>
  are only positive or negative whole numbers<br>
  discrete values<br>
  int(x) to cast an int or round a float<br>
  indexing with square brackets requires int<br>
  
### <a id='s15-0-3' />float
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
    
### <a id='s15-0-4' />boolean
  True or False<br>
  1 or 0<br>
  full or empty values<br>
  binary in nature<br>
  not negates bool<br>
  result of <, >, >=, <=, == is always boolean<br>
  
### <a id='s15-0-5' />string
  collection of characters<br>
  concatenation +<br>
  str() to cast<br>
  
### <a id='s15-0-6' />None
  describes the absence of a value<br>
  functions auto return None if no return statement or empty return statement<br>
  None can be used as a placeholder<br>
  can sub for a n/a data (missing data)<br>
 
______________________________________________________________________________________________________

# <a id='s16' />Numpy
### <a id='s16-0-1' />numpy arrays
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
  
### <a id='s16-0-2' />2D numpy arrays
  .shape => returns (rows, cols); not a method, is an attribute<br>
  array[0][2] == array[0,2]<br>
  calling just cols or rows is easy -> array[r:c] with slicing telling python to include all<br>
  ie. np_baseball[:,1] select just the 2nd column<br>
      print(np_baseball[123,0]) print the 124th player's height<br>
  Can create an array of conversions by row/col and multiply<br>
    ie. array with 3 cols, new array with conversion factors in 3 cols, multiply to convert whole array<br>

### <a id='s16-0-3' />basic statistics
  np.mean(array[:,0])<br>
  np.median(array[:])<br>
  np.corrcoef(array1, array2). see if 2 array rows/cols are correlaed<br>
  np.std(array) std dev<br>
  np.sum()<br>
  np.sort()<br>
  Very fast calculations because all 1 data type<br>
  
  ______________________________________________________________________________________________________
  
# <a id='s17' />Numbers and Booleans
= += -= *= /= **=<br>
+ - * / // **<br>
// floor division<br>
% remainder (mod)<br>
== finds relation between two booleans, relational operator<br>
!= result type: boool; "not equal to"<br>
< <= > >=<br>
and, or ->> bool op used to preform logical conjuction<br>
#### <a id='s' />not:
 returns True when op is false orr 0, vice versa<br>
#### <a id='s' />del: 
removes item/element at a specified index location from lis, not returned; takes index as arg, deletes itema at index<br>
#### <a id='s' />int: 
num w/o decimal, +/-<br>
#### <a id='s' />float:
 num with decimal, +/- (always returned by /)<br>
#### <a id='s' />True:
 bool(1)<br>
#### <a id='s' />False:
 0, None, len() ie. [] or " ", bool(0)<br>

# <a id='s18' />Basic Operators
### <a id='s18-0-1' />// floor division
  if either is a float, will return a float<br>

### <a id='s18-0-2' />% modulus
  trial division: see if divides in evenly, common step to find primes and all divisors of 

### <a id='s18-0-3' />given num
  parity: mod 2, whether an integer is even or odd  <br>
  if either is a float, will return a float<br>
  
### <a id='s18-0-4' />Order of op
  PEMDAS, M includes %<br>
  if same precedence, left to right<br>
  
### <a id='s18-0-5' />Logical ops
  and, or, !<br>
  btwise: & = and, |. = or, ~ = not<br>
    exclusive or (^) = only when 1 op is true (vs or where bith can be true<br>
  not evaluated 1st, then and, or last<br>
  bitwise 1st, then logical op<br>
  excl or befor or<br>
  
### <a id='s18-0-6' />comparison ops
  < > <= >= == !=

  ______________________________________________________________________________________________________

# <a id='s19' />Control Flow
if (any expression that resolves as either True or False) --> condition<br>
else ==> under all other conditions<br>


  ______________________________________________________________________________________________________

# <a id='s20' />GitHub Commands Terminal

  ______________________________________________________________________________________________________


# <a id='s21' />List Basics
A list is a collection of arbitrary objects, often called an array in other programming languages. The contents of a list can be thought of as ordered, in that a list guarantees that its contents are numerically indexed. The items, or elements of a list can be accessed by the numeric index. In Python, a list is mutable in the sense that its contents can be rearranged, replaced, or deleted. A list can be nested to arbitrary depth. The list datatype is the primary construct on which you will perform iteration, or going item-by-item across a data structure.<br>

### <a id='s21-0-1' />LISTS ARE MUTABLE

### <a id='s21-0-2' />creating a list:
  some_list = []
  some_list = [x,y,z]
  some_list = list()
  some_list = list(some_other_collection)

### <a id='s21-0-3' />calling an elem from a list:
  my_list[index_of_elem]

  note:
    -1 as index will call last elem in list
    
    indexing begins at 0

### <a id='s21-0-4' />changing elem in list at index:
    <list_name>[<index_of_element_to_change>] = <new_value_for_index>

### <a id='s21-0-5' />concatenating lists:
  can concatenate lists with '+' operator

      ``` python
      first_list = ['This', 'is', 'list', '1']
      second_list = ['add', 'me', 'to', 'list', '1']

      concatenated_list = first_list + second_list

      # This will print ['This', 'is', 'list', '1', 'add', 'me', 'to', 'list', '1']
      print(concatenated_list)
      ```

### <a id='s21-0-6' />list memembership:
  elem in lst
      checks if in list, and returns bool True if so
  elem not in lst
      checks if in list, returns bool True if not

### <a id='s21-0-7' />list slicing:
  sublst[start:stop]
  sublst[negative_start: negative_stop]

  ...where:
      start is an index at which our "slice" will begin
      stop is also an index before which our "slice" will end
      Thus, start will be included in the sublist, but stop will not be
  OR:
      negative_start is a negative index at which our "slice" will begin
      negative_stop is also a negative index after which our "slice" will end
      Thus, negative_start will be included in the sublist, but negative_stop will not be

### <a id='s21-0-8' />nested lists:
  ####creating:
  ``` python
      nested_list_example_2 = [list(), list(), list()]
    # OR
      nested_list_example_3 = [[], [], []]
  ```
  #### accessing:
    ```python
    nested_list = [['a', 'b', 'c'], [1, 2, 3]]

    # Use indexing to access the second element in the first nested list<br>
    element_within_nested_list = nested_list[0][1]<br>
    print(element_within_nested_list)
    

    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in nums:
      for j in i:
        print(j)
        ```


  ####slicing:
  ```python
    start = 10
    end = 21

    num_list = list(range(start, end))
    overall_list = [['a', 'b', 'c'], num_list, [6, 7, 8]]

    # Assign and print the elements in indeces 2, 3, 4, 5, 6 from num_list
    sublist = overall_list[1][2:7]
    print(sublist)
  ```

### <a id='s21-0-9' />unpacking a list:
  some_list = ['pig', 'boar', 'elephant']
  a, b, c = some_list

  #a = 'pig, b = 'boar', c='elephant'

### <a id='s21-0-10' />functions and methods

#### <a id='s' />range([start], stop[, step]):
  start: Starting number of the sequence.
  stop: Generate numbers up to, but not including this number.
  step: Difference between each number in the sequence.
  
  Note that:

  All parameters must be integers.
  All parameters can be positive or negative.
  range() (and Python in general) is 0-index based, meaning list indexes start at 0, not 1. eg. The syntax to access the first element of a list is mylist[0]. Therefore the last integer generated by range() is up to, but not including, stop. For example range(0, 5) generates integers from 0 up to, but not including, 5.

#### <a id='s' />.copy()
  equivalent to:
  lst[:]

#### <a id='s' />.index(elem)
  returns the index of first instance of element in list

#### <a id='s' />.append(elem)
  adds element to end of list

#### <a id='s' />.extend(lst)
  extends current list by argument list

#### <a id='s' />.remove(elem)
  removes first instance of element

#### <a id='s' />del
  del lst[i]<br>
  deleted element at specified index

#### <a id='s' />len(lst)
  returns the length of the argument list

#### <a id='s' />sum(lst)
  returns numeric sum of all elements in list

#### <a id='s' />sorted(lst)
  returns a sorted version of argument list <br>
  MUST BE SAVED TO NEW VAR TO REMAIN PERMENANT, does not make any permenant changes to original list

#### <a id='s' />.sort()
  sorts original list permenantly


#### <a id='s' />reversed(lst)
  returns reversed version of argument list <br>
  MUST BE SAVED TO NEW VAR TO REMAIN PERMENANT, does not make any permenant changes to original list
  Also, must be cast to list with [] as returns reversed obj rather than list

#### <a id='s' />.reverse()
  reverses original list permenantly

#### <a id='s' />max(lst)
  returns max num in list

#### <a id='s' />min(lst)
  returns min num in list

#### <a id='s' />any(lst)
  returns bool True if any elem in list are truthy

#### <a id='s' />all(lst)
  returns bool True only if ALL elem in list are truthy

#### <a id='s' />.pop()
  removes last elem in list, returns elem

#### <a id='s' />.count(elem)
  returns count of elem in lst

#### <a id='s' />enumerate
  for i, elem in enumerate(list):
    iterates through both i and elem in list
  
#### <a id='s' />zip 
  for a,b,c in zip(list_1, list_2, range(len(list_3))):
    #iterates through parallel lists at same time

______________________________________________________________________________________________________


# <a id='s22' />accumulators:
  ### PATTERN:
      Initialize an accumulator variable

      Repeat:
          Modify the accumulator variable

      When the above loop terminates, accumulator has the correct value

### <a id='s22-0-1' />examples:
```python
<a id='s23' />#int:
num_list = [1, 2, 3, 4, 5]

num_sum = 0
for num in num_list:
    num_sum += num

print(num_sum)


<a id='s24' />#float:
num_list = [1.6, -2.25, 3.61, 4.01, 5.93]

num_sum = 0.0
for num in num_list:
    num_sum += num

print(num_sum)

#bool <a id='s25' />flags:
lst = [23, 42, 86, 92, 93, 94]

has_value_over_90 = False
for val in lst:
    if val > 90:
        has_value_over_90 = True
        break

print(has_value_over_90)

<a id='s26' />#list
num_list = [2, 12, 12, 1, 24, 10, 19, 17, 8, 8, 25, 14, 12, 4, 23, 14, 18, 13, 0, 15, 22, 8, 5, 12, 6]

altered_num_list = []
for num in num_list:
    if num % 2 == 0:
        altered_num_list.append(num**2)
    else:
        altered_num_list.append(num**3)

#flattened <a id='s27' />nested lists
mixed_list = ['word', [1, 2, 3, 4, 5], 43, 90.0]
flattened = []

for item in mixed_list:
    if isinstance(item, list):
        for nested_item in item:
            flattened.append(nested_item)
    else:
        flattened.append(item)

#parallell <a id='s28' />lists:   
  #enumerate
    def polynomial(coefs, x):
    res = 0
    n = len(coefs) - 1 # The degree of the polynomial

    for idx, val in enumerate(coefs):
        res += val * x**(n - idx)

    return res


  #zip     
    odds = []
    lst_a = [1, 32, 15, 7, 3, 9, 16, 13, 22, 8]
    lst_b = [51, 6, 25, 2, 18, 19, 21, 14, 4, 11]

    for a, b in zip(lst_a, lst_b):
        if a % 2 == 1:
            odds.append(a)
        if b % 2 == 1:
            odds.append(b)

```
______________________________________________________________________________________________________

# <a id='s29' />iteration with for loops
  initialize a variable to be accumulated, then in a for/while loop accumulate as you iterate through

  #### for char in string:
    #iterates through every character in string

  #### for word in phrase:
    #iterates through every word in sentence as separated by whitespace chars 

  #### for num in range(0, 100):
    #iterates through nums 0-99
  
  #### for i in range(len(list)):
    #iterated through indexes of list from 0 to len(list)
  
  #### for elem in list:
    #iterates through all elements of list

  #### for i, elem in enumerate(list):
    iterates through both i and elem in list
  
  #### for a,b,c in zip(list_1, list_2, range(len(list_3))):
    #iterates through parallel lists at same time

______________________________________________________________________________________________________

# <a id='s30' />break, continue, pass

  break and continue are commonly used within loops to either bypass some code or exit the loop itself. There are a number of reasons you may want to do this, either to optimize your code, or to prevent further or unnecessary calculation. In general pass can be seen as a placeholder for code in order to allow your function or loop to run.

### <a id='s30-0-1' />break out of for loop:
```python
# <a id='s31' />this for loop will exit after 50
for num in range(100):
    print(num)

    if num == 50:
        break

def is_prime(n):
    prime = True

    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

    return prime

#break <a id='s32' />out of while loop
while True: # note, infinite loop
    input = input('Do you want to continue looking at this message? Spell the word "commitment" correctly in order to exit, otherwise we\'re doing this forever... ')

    if input == 'commitment':
        break
```

### <a id='s32-0-1' />continue for skipping loops:
```python
not_squares = []

def is_square(num):
    for i in range(2, num):
        if i**2 == num:
            return True
        if i**2 > num:
            break

    return False


for num in range(2, 101):
    if is_square(num) == True:
        continue
    not_squares.append(num)

print(not_squares)
```

### <a id='s32-0-2' />pass:
used as a place holder in an unfinished function

______________________________________________________________________________________________________

# <a id='s33' />while loops

## <a id='s33-1' />You should only use a while loop when the number of iterations of the loop is not known. 

```python
def greatest_common_divisor(num_1, num_2):
    """
    Calculate the Greatest Common Divisor of num_1 and num_2.
    """
    runs = 0
    while num_2 != 0:
        runs += 1
        num_1, num_2 = num_2, num_1 % num_2

        print(runs, ' iterations')
    return num_1

print(greatest_common_divisor(121, 55))
print(greatest_common_divisor(75, 50))
print(greatest_common_divisor(999, 33))
print(greatest_common_divisor(27, 17))
```

watch out for infinite while loops, add in breaks when certain conditions are met to avoid

```python
# <a id='s34' />define a counter
loops = 0

# <a id='s35' />notice that setting x to 2 will allow entrance into the while
x = 2

# <a id='s36' />put the counter in the `while` to avoid an infinite loop
while x < 3:
    print(x)

    # this condition will ensure that the while exits
    if loops > 20:
        break

    # make sure to increment the loops variable
    loops += 1
  ```

### <a id='s36-0-1' />while loop using conditional check:
  while True: do something
    x = 20

    while x > 0:
        print(x)

        x -= 1

#### <a id='s' />another example:
  def get_menu_item():
    menu = '''Choose an item:
              (1) broccoli
              (2) carrots
              (3) cabbage
              choice:  '''

    choice = int(input(menu))
    items = ['broccoli', 'carrots', 'cabbage']
    return items[choice-1]

orders = []

cont = 'y'
while cont == 'y':
    orders.append(get_menu_item())

    # order_max -= 1
    cont = input('order more? ')

print(orders)

### <a id='s36-0-2' />open-ended problems:
```python
from random import choice

def get_sample(lower=1, upper=100):
    return choice(range(1, upper+1))

def get_sample_counts(m, threshold):
    output = []

    for _ in range(m):
        num_trials = 1
        while True:
            sample = get_sample()

            if sample < threshold:
                output.append(num_trials)
                break
            else:
                num_trials += 1

    return output


sample_trials = get_sample_counts(100, 25)

# <a id='s37' />Make the index of counts correspond with the
# <a id='s38' />number of trials
counts = [0]*(max(sample_trials) + 1)

for trial in sample_trials:
    counts[trial] += 1

# <a id='s39' />Make a simple terminal graphic to display the distribution
# <a id='s40' /> of number of trials needed to achieve a value
# <a id='s41' /> below a given threshold.
for i, count in enumerate(counts):
    if i == 0:
        continue
    print('{:4d}: {}'.format(i, '*' * count))
```

### <a id='s41-0-1' />for or while?
    The previous lessons have talked extensively about when to not use a while loop. Essentially, avoid using while loops, unless they are specifically appropriate.

    ####while for menus and open-ended problems
    When you need to create a menu but you don't know how many selections will need to be made from that menu, a while loop is very appropriate. In addition, if you don't know how long your algorithm will need to run to be able to solve a particular problem, then a while loop is likely an appropriate approach.

    ####for loops if you know how many times the loop should run
    In many cases you will use a for loop to traverse a list. If you have a populated list, then you know how many items are in that list, which means you most likely know how many times your loop should run. In these cases, you will almost always use a for loop.

    In other cases, you may use a for loop to perform an action some x number of times. You can use for i in range(x): do something to perform this operation.