# What is Data Science?
### data types:
 working with text and data<br>
### variables:
 storing data <br>
### lists:
 working with data in an ordered collection<br>
### dictionaries:
 representing data as a collection of attributes<br>
### loops and iteration:
 repeating a sequence of instructions <br>
### data visualization:
 using plots to display data <br>
### functions:
 defining and running specific procedures in code <br>

### to find all methods for a data type:
  print(dir(datatype))

#### isinstance(elem, type)
  returns bool True if same type
  returns bool False if different type

#### type(elem)
  returns <class type>
______________________________________________________________________________________________________

# String Methods
### Strings are sequences
    Recall from earlier that strings are a sequence type in Python, but they are also immutable. This means they can be iterated through and sliced, for example, but do not support indexed reassignment or the del statement.

### declaring a string
  string = ''
  string = ""
  casting  -- > str(element_to_be_cast)

### repetition
  string*num repeats string num number of times

### containment
  "p" in "python"
    returns True

### [instance of dataype].[method]()

#### str.upper() <br>

#### str.lower() <br>

#### str.title() <br>
 
#### str.endswith()  <br>
  returns a boolean <br>

#### str.replace(x, y)<br>
  ie. "Homer" ->> replace('o', 'O')<br>
      returns "HOmer"<br>
      
#### help(str)<br>
   returns directory of str commands (exit w/ q)<br>

#### str.capitalize()<br>

#### string slicing:<br>
  [2:4] = [incl, ecl]<br>
  ie. in carrot, would return 'rr'<br>
  [4] would return 4th char<br>
 
#### concatenation:<br>
  'xyz' + '123'<br>
  returns 'xyz123'<br>
  
#### fstring: print(f"... {} ...")

#### .split([separator [, maxsplit]])<br>
  braks up str at specified separator<br>
  returns list of stirngs<br>
  seperator (optional): if not specified, any whitespace<br>
  maxsplit (optional): defines max number of splits; default is -1 meaning no limit<br>
  
#### .count(substring, start=..., end=...)<br>
  searches substring and returns # of instances

#### .format<br>
  "single_and_escaped = 'I won\'t use anything other than single quotes!"

#### .isspace()
  checks if character is a whitespace char liek ' ', '\t', '\n', '\r' etc

#### .index(substring[, start[, end]])<br>
  substring: to be search in str<br>
  start/end: (optional) within str [st:end]<br>
  returns lowed index in str where found<br>

#### .isalnum()<br>
  returns True is all char alphaneumeric<br>
  
#### .isalpha()<br>
  returns True if all char in alphabets<br>

#### .is digit()

#### .isnumeric()

#### .join(iterable)<br>
  "".join(lst)

  returns str by joining all elelments of an iterable, separated by a str separator<br> (concatenates)<br>
  data types: list, tuple, string, dict, set<br>
  file obj + obj defined with __iter__() or __getitem()__ method<br>

#### .replace(old, new[, count])<br>
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

#### .append(item)<br>
  item added to end of th elist<br>
  can be any datatype<br>
  returns None
  
#### .clear()<br>
  removes all items from the list<br>
  
#### .copy()<br>
  copies old list to new list, changes to new list won't effect old list (unlike =)<br>
  also can use slicing (new_list = list[:])
  
#### .count(element)<br>
  returns # of times element is in list<br>
  can be used with nested lists and tuples
  
#### .extend(iterable)<br>
  adds all the elements of an iterable (list, tuple, string, etc) to the end of the list<br>
  Modifies original list, does not return value<br>
  also can append all elements to list using: + +=<br>
  list slicing: <br>
    a = [1,2]; b = [3,4]<br>
    a[len(a):] = b<br>
    a = [1, 2, 3, 4]<br>
  merges rather than append<br>
  
#### .index(element, start, end)<br>
  returns the index of the specified element in the list<br>
  element: element to be searched<br>
  start (op): start from this index<br>
  end (op): search up to this index<br>
  returns index of given element OR ValueEror if not found<br>
  *only returns 1st occurane of element
  
#### .insert(i, elem)<br>
  inserts element into list @ ith index<br>
  all elements after elem shifted to right<br>
  returns None, updates current list<br>
  *can insert Tuples as elements
  
#### .pop(index)<br>
  removes and returns an element at a given index from a list<br>
  if index not passed, returns for (-1)
  
#### .remove(element)<br>
  removes the first matching element (which is passed as an arg) from list<br>
  throws error if element DNE<br>
  returns None, or error<br>
  if need to delete elements based on index, use .pop()
  
#### .reverse()<br>
  reverses the elements of the list<br>
  returns None<br>
  can also do with slicing operator: reversed_list = list [::-1]<br>
  accessing items in reversed order: for x in reversed(list):<br>
  
#### .sort(key=..., reverse=...)<br>
  key (op): func that serves as key for he sort comparison<br>
  reverse (op): if True, sorted list is sorted in descending order<br>
  changes original list<br>
  no return<br>
  to return sorted list (with original unchanged) use sorted()<br>
  ie. list.sort(key = len, reverse = true/false)<br>
      OR sorted(list, key=len)<br>
  
______________________________________________________________________________________________________

# Dictionaries


### func(arg, arg)['name']

#### .clear()<br>
  removes all items from dict
  
#### .copy()<br>
  returns shallow copy of dict<br>
  doesn't change original dict (unlike =)
  
#### .fromkeys(sequence[, value])<br>
  creates new dict from given sequence of elements with value provided by user<br>
  sequence: sequence of elements which is to be used as keys for new dict<br>
  value (op): value which is set to each element of dict<br>
  
#### .get(key[, value])<br>
  returns value for specific key, if key is in dict<br>
  key: key to be searched in dict<br>
  value (op): value to be returned if key is not found; defaults to None<br>
  
#### .items()<br>
  returns a view object that displays a list of dict key, value tuple pairs
  
______________________________________________________________________________________________________

# Variables

______________________________________________________________________________________________________

# Scalar Types
ints, floats, bools, str, None, complex, bytes<br>
### scalar type:
 holds a single value (vs. collection type, which holds many values and can be changed w/p id value change -> ie. not being destroyed and remade)<br>
  scalar types in python are immutable, they are detroyed and remade everytime the value is reassigned<br>
  
### int<br>
  can represent a value that is countable<br>
  are only positive or negative whole numbers<br>
  discrete values<br>
  int(x) to cast an int or round a float<br>
  indexing with square brackets requires int<br>
  
### float<br>
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
    
### boolean<br>
  True or False<br>
  1 or 0<br>
  full or empty values<br>
  binary in nature<br>
  not negates bool<br>
  result of <, >, >=, <=, == is always boolean<br>
  
### string<br>
  collection of characters<br>
  concatenation +<br>
  str() to cast<br>
  
### None<br>
  describes the absence of a value<br>
  functions auto return None if no return statement or empty return statement<br>
  None can be used as a placeholder<br>
  can sub for a n/a data (missing data)<br>
 
______________________________________________________________________________________________________

# Numpy
### numpy arrays<br>
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
  
### 2D numpy arrays<br>
  .shape => returns (rows, cols); not a method, is an attribute<br>
  array[0][2] == array[0,2]<br>
  calling just cols or rows is easy -> array[r:c] with slicing telling python to include all<br>
  ie. np_baseball[:,1] select just the 2nd column<br>
      print(np_baseball[123,0]) print the 124th player's height<br>
  Can create an array of conversions by row/col and multiply<br>
    ie. array with 3 cols, new array with conversion factors in 3 cols, multiply to convert whole array<br>

### basic statistics<br>
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
#### not:
 returns True when op is false orr 0, vice versa<br>
#### del: 
removes item/element at a specified index location from lis, not returned; takes index as arg, deletes itema at index<br>
#### int: 
num w/o decimal, +/-<br>
#### float:
 num with decimal, +/- (always returned by /)<br>
#### True:
 bool(1)<br>
#### False:
 0, None, len() ie. [] or " ", bool(0)<br>

# Basic Operators
### // floor division<br>
  if either is a float, will return a float<br>

### % modulus<br>
  trial division: see if divides in evenly, common step to find primes and all divisors of 

### given num<br>
  parity: mod 2, whether an integer is even or odd  <br>
  if either is a float, will return a float<br>
  
### Order of op<br>
  PEMDAS, M includes %<br>
  if same precedence, left to right<br>
  
### Logical ops<br>
  and, or, !<br>
  btwise: & = and, |. = or, ~ = not<br>
    exclusive or (^) = only when 1 op is true (vs or where bith can be true<br>
  not evaluated 1st, then and, or last<br>
  bitwise 1st, then logical op<br>
  excl or befor or<br>
  
### comparison ops<br>
  < > <= >= == !=

  ______________________________________________________________________________________________________

# Control Flow
if (any expression that resolves as either True or False) --> condition<br>
else ==> under all other conditions<br>


  ______________________________________________________________________________________________________

# GitHub Commands Terminal

  ______________________________________________________________________________________________________


# List Basics
A list is a collection of arbitrary objects, often called an array in other programming languages. The contents of a list can be thought of as ordered, in that a list guarantees that its contents are numerically indexed. The items, or elements of a list can be accessed by the numeric index. In Python, a list is mutable in the sense that its contents can be rearranged, replaced, or deleted. A list can be nested to arbitrary depth. The list datatype is the primary construct on which you will perform iteration, or going item-by-item across a data structure.<br>

### LISTS ARE MUTABLE

### creating a list:
  some_list = []
  some_list = [x,y,z]
  some_list = list()
  some_list = list(some_other_collection)

### calling an elem from a list:
  my_list[index_of_elem]

  note:
    -1 as index will call last elem in list
    
    indexing begins at 0

### changing elem in list at index:
    <list_name>[<index_of_element_to_change>] = <new_value_for_index>

### concatenating lists:
  can concatenate lists with '+' operator

      ``` python
      first_list = ['This', 'is', 'list', '1']
      second_list = ['add', 'me', 'to', 'list', '1']

      concatenated_list = first_list + second_list

      # This will print ['This', 'is', 'list', '1', 'add', 'me', 'to', 'list', '1']
      print(concatenated_list)
      ```

### list memembership:
  elem in lst
      checks if in list, and returns bool True if so
  elem not in lst
      checks if in list, returns bool True if not

### list slicing:
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

### nested lists:
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

### unpacking a list:
  some_list = ['pig', 'boar', 'elephant']
  a, b, c = some_list

  #a = 'pig, b = 'boar', c='elephant'

### functions and methods

#### range([start], stop[, step]):
  start: Starting number of the sequence.
  stop: Generate numbers up to, but not including this number.
  step: Difference between each number in the sequence.
  
  Note that:

  All parameters must be integers.
  All parameters can be positive or negative.
  range() (and Python in general) is 0-index based, meaning list indexes start at 0, not 1. eg. The syntax to access the first element of a list is mylist[0]. Therefore the last integer generated by range() is up to, but not including, stop. For example range(0, 5) generates integers from 0 up to, but not including, 5.

#### .copy()
  equivalent to:
  lst[:]

#### .index(elem)
  returns the index of first instance of element in list

#### .append(elem)
  adds element to end of list

#### .extend(lst)
  extends current list by argument list

#### .remove(elem)<br>
  removes first instance of element

#### del<br>
  del lst[i]<br>
  deleted element at specified index

#### len(lst)
  returns the length of the argument list

#### sum(lst)
  returns numeric sum of all elements in list

#### sorted(lst)
  returns a sorted version of argument list <br>
  MUST BE SAVED TO NEW VAR TO REMAIN PERMENANT, does not make any permenant changes to original list

#### .sort()
  sorts original list permenantly


#### reversed(lst)
  returns reversed version of argument list <br>
  MUST BE SAVED TO NEW VAR TO REMAIN PERMENANT, does not make any permenant changes to original list
  Also, must be cast to list with [] as returns reversed obj rather than list

#### .reverse()
  reverses original list permenantly

#### max(lst)
  returns max num in list

#### min(lst)
  returns min num in list

#### any(lst)
  returns bool True if any elem in list are truthy

#### all(lst)
  returns bool True only if ALL elem in list are truthy

#### .pop()
  removes last elem in list, returns elem

#### .count(elem)
  returns count of elem in lst

#### enumerate
  for i, elem in enumerate(list):
    iterates through both i and elem in list
  
#### zip 
  for a,b,c in zip(list_1, list_2, range(len(list_3))):
    #iterates through parallel lists at same time

______________________________________________________________________________________________________


# accumulators:
  ### PATTERN:
      Initialize an accumulator variable

      Repeat:
          Modify the accumulator variable

      When the above loop terminates, accumulator has the correct value

### examples:
```python
#int:
num_list = [1, 2, 3, 4, 5]

num_sum = 0
for num in num_list:
    num_sum += num

print(num_sum)


#float:
num_list = [1.6, -2.25, 3.61, 4.01, 5.93]

num_sum = 0.0
for num in num_list:
    num_sum += num

print(num_sum)

#bool flags:
lst = [23, 42, 86, 92, 93, 94]

has_value_over_90 = False
for val in lst:
    if val > 90:
        has_value_over_90 = True
        break

print(has_value_over_90)

#list
num_list = [2, 12, 12, 1, 24, 10, 19, 17, 8, 8, 25, 14, 12, 4, 23, 14, 18, 13, 0, 15, 22, 8, 5, 12, 6]

altered_num_list = []
for num in num_list:
    if num % 2 == 0:
        altered_num_list.append(num**2)
    else:
        altered_num_list.append(num**3)

#flattened nested lists
mixed_list = ['word', [1, 2, 3, 4, 5], 43, 90.0]
flattened = []

for item in mixed_list:
    if isinstance(item, list):
        for nested_item in item:
            flattened.append(nested_item)
    else:
        flattened.append(item)

#parallell lists:   
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

# iteration with for loops
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

# break, continue, pass

  break and continue are commonly used within loops to either bypass some code or exit the loop itself. There are a number of reasons you may want to do this, either to optimize your code, or to prevent further or unnecessary calculation. In general pass can be seen as a placeholder for code in order to allow your function or loop to run.

### break out of for loop:
```python
# this for loop will exit after 50
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

#break out of while loop
while True: # note, infinite loop
    input = input('Do you want to continue looking at this message? Spell the word "commitment" correctly in order to exit, otherwise we\'re doing this forever... ')

    if input == 'commitment':
        break
```

### continue for skipping loops:
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

### pass:
used as a place holder in an unfinished function

______________________________________________________________________________________________________

# while loops

## You should only use a while loop when the number of iterations of the loop is not known. 

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
# define a counter
loops = 0

# notice that setting x to 2 will allow entrance into the while
x = 2

# put the counter in the `while` to avoid an infinite loop
while x < 3:
    print(x)

    # this condition will ensure that the while exits
    if loops > 20:
        break

    # make sure to increment the loops variable
    loops += 1
  ```

### while loop using conditional check:
  while True: do something
    x = 20

    while x > 0:
        print(x)

        x -= 1

#### another example:
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

### open-ended problems:
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

# Make the index of counts correspond with the
# number of trials
counts = [0]*(max(sample_trials) + 1)

for trial in sample_trials:
    counts[trial] += 1

# Make a simple terminal graphic to display the distribution
#  of number of trials needed to achieve a value
#  below a given threshold.
for i, count in enumerate(counts):
    if i == 0:
        continue
    print('{:4d}: {}'.format(i, '*' * count))
```

### for or while?
    The previous lessons have talked extensively about when to not use a while loop. Essentially, avoid using while loops, unless they are specifically appropriate.

    ####while for menus and open-ended problems
    When you need to create a menu but you don't know how many selections will need to be made from that menu, a while loop is very appropriate. In addition, if you don't know how long your algorithm will need to run to be able to solve a particular problem, then a while loop is likely an appropriate approach.

    ####for loops if you know how many times the loop should run
    In many cases you will use a for loop to traverse a list. If you have a populated list, then you know how many items are in that list, which means you most likely know how many times your loop should run. In these cases, you will almost always use a for loop.

    In other cases, you may use a for loop to perform an action some x number of times. You can use for i in range(x): do something to perform this operation.