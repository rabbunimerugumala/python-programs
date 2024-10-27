#             ♦ PYTHON NOTES ♦

## Introduction To Python

 1.Python is a widely used general-purpose, high level programming language. 
 It was created by Guido van Rossum in 1991 and further developed by the Python 
   Software Foundation. It was designed with an emphasis on code readability, and 
   its syntax allows programmers to express their concepts in fewer lines of code.

 2.Python is a programming language that lets you work quickly and integrate systems
  more efficiently
---
## Python Keywords:-

 > Keywords in Python are reserved words that can not be used as a variable name,
   function name, or any other identifier


- and           - This is a logical operator which returns true if both the operands are    
                 true else  returns false. 

- or	           - This is also a logical operator which returns true if anyone operand is  
                 true else returns false.

- not	         - This is again a logical operator it returns True if the operand is false 
                 else returns false.

- if	           - This is used to make a conditional statement.

- elif	       - Elif is a condition statement used with an if statement. The elif 
                 statement is executed if the previous conditions were not true.

- else	       - Else is used with if and elif conditional statements. The else block is 
                 executed if the given condition is not true.

- for	       - This is used to create a loop.

- while	       - This keyword is used to create a while loop.

- break	       - This is used to terminate the loop.

- as	           - This is used to create an alternative.

- def	       - It helps us to define functions.

- lambda	       - It is used to define the anonymous function.

- pass	       - This is a null statement which means it will do nothing.

- return        - It will return a value and exit the function.

- True	       - This is a boolean value.

- False	       - This is also a boolean value.

- try	       - It makes a try-except statement.

- with	       - The with keyword is used to simplify exception handling.

- assert	       - This function is used for debugging purposes. Usually used to check the correctness of code.

- class	       - It helps us to define a class.

- continue	   - It continues to the next iteration of a loop

- del	       - It deletes a reference to an object.

- except	     - Used with exceptions, what to do when an exception occurs

- finally	   - Finally is used with exceptions, a block of code that will be executed no 
                 matter if there is an exception or not.

- from	       - It is used to import specific parts of any module.

- global	     - This declares a global variable.

- import	     - This is used to import a module.

- in	          - It’s used to check whether a value is present in a list, range, tuple, etc.

- is	          - This is used to check if the two variables are equal or not.

- none	       - This is a special constant used to denote a null value or avoid. It’s  
                important toremember, 0, any empty container(e.g empty list) do not compute to None.

- nonlocal	   - It’s declared a non-local variable.

- raise	       - This raises an exception.

- yield	       - It ends a function and returns a generator.

- async	       - It is used to create asynchronous coroutine.

- await	       - It releases the flow of control back to the event loop.
---

## Python print()  
### Function Syntax
- Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
Parameters: 
- value(s): Any value, and as many as you like. Will be converted to a string before printed
- sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default  :’ ‘
- end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
- file     : (Optional) An object with a write method. Default :sys.stdout
- flush    : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

Return Type: It returns output to the screen. 

#EXAMPLE PROGRAM
 <print("python language!")
#OUTPUT:
  python language!

 <print("I am learning Python")
#ONTPUT:
  I am learning Python


 <Examples of how to print the rest of Python's built-in data types..

>#how to print ints
>>print(7) #output is 7

>#how to print floats
print(7.0) #output is 7.0

>#how to print complex
>>print(1j) #output is 1j

>#how to print a list
>>print([10,20,30]) #output is [10,20,30]

>#how to print a tuple
>>print((10,20,30)) #output is (10,20,30)

>#how to print a dictionary
>>print({"language": "Python", "field": "data science"})
#output is {"language": "Python", "field": "data science"}

>#how to print a set
>>print({"autumn","winter","spring","summer"})
#output is {"autumn","winter","spring","summer"}

>#how to print a bool
>>print(True) #output is True
>>print(False) #output is False

---

## List Methods in Python:- 

- 	append()  : Used for appending and adding elements to the end of the List. 
-   copy()	  : It returns a shallow copy of a list.
-  clear()	  : This method is used for removing all items from the list. 
-  count()	  : These methods count the elements.
-   extend()	: Adds each element of the iterable to the end of the List.
-  index()	  : Returns the lowest index where the element appears. 
-   insert()	: Inserts a given element at a given index in a list. 
-  pop()	    : Removes and returns the last value from the List or the given index value.
-   remove()	: Removes a given object from the List. 
-  reverse()	: Reverses objects of the List in place.
-   sort()	  : Sort a List in ascending, descending, or user-defined order.

>append(self, object, /)
 >      Append object to the end of the list.
 >
 >  clear(self, /)
 >      Remove all items from list.
 >
 >  copy(self, /)
 >      Return a shallow copy of the list.
 >
 >  count(self, value, /)
 >      Return number of occurrences of value.
 >
 >  extend(self, iterable, /)
 >      Extend list by appending elements from the iterable.
 >
 >  index(self, value, start=0, stop=9223372036854775807, /)
 >      Return first index of value.
 >
 >      Raises ValueError if the value is not present.
 >
 >  insert(self, index, object, /)
 >      Insert object before index.
 >
 >  pop(self, index=-1, /)
 >      Remove and return item at index (default last).
 >
 >      Raises IndexError if list is empty or index is out of range.
 >
 >  remove(self, value, /)
 >      Remove first occurrence of value.
 >
 >      Raises ValueError if the value is not present.
 >
 >  reverse(self, /)
 >      Reverse *IN PLACE*.
 >
 >  sort(self, /, *, key=None, reverse=False)
 >      Sort the list in ascending order and return None.
 >
 >      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 >      order of two equal elements is maintained).
 >
 >      If a key function is given, apply it once to each list item and sort them,
 >      ascending or descending, according to their function values.
 >
 >      The reverse flag can be set to sort in descending order.
---

 ## Python Tuple Methods

- count()  : 	Returns the number of times a specified value occurs in a tuple
- index()  : 	Searches the tuple for a specified value and returns the position of where it 
            was found               
  
 >  count(self, value, /)
 >      Return number of occurrences of value.
 >
 >  index(self, value, start=0, stop=9223372036854775807, /)
 >      Return first index of value.
 >
 >   Raises ValueError if the value is not present.

---

## Python Set Methods

- add()                         :  Adds an element to the set
- clear()                       :  Removes all the elements from the set
- copy()                        :  Returns a copy of the set
- difference()                  :  Returns a set containing the difference between two or more sets
- difference_update()           :  Removes the items in this set that are also included in another, specified set
- discard()                     :  Remove the specified item
- intersection()                :  Returns a set, that is the intersection of two or more sets
- intersection_update()         :  Removes the items in this set that are not present in other, specified set(s)
- isdisjoint()                  :  Returns whether two sets have a intersection or not
- issubset()                    :  Returns whether another set contains this set or not
- issuperset()                  :  Returns whether this set contains another set or not
- pop()                         :  Removes an element from the set
- remove()                      :  Removes the specified element
- symmetric_difference()        :  Returns a set with the symmetric differences of two sets
- symmetric_difference_update() :  inserts the symmetric differences from this set and another
- union()                       :  Return a set containing the union of sets
- update()                      :  Update the set with another set, or any other iterable

 >  add(...)
 >      Add an element to a set.
 >
 >      This has no effect if the element is already present.
 >
 >  clear(...)
 >      Remove all elements from this set.
 >
 >  copy(...)
 >      Return a shallow copy of a set.
 >
 >  difference(...)
 >      Return the difference of two or more sets as a new set.
 >
 >      (i.e. all elements that are in this set but not the others.)
 >
 >  difference_update(...)
 >      Remove all elements of another set from this set.
 >
 >  discard(...)
 >      Remove an element from a set if it is a member.
 >
 >      Unlike set.remove(), the discard() method does not raise
 >      an exception when an element is missing from the set.
 >
 >  intersection(...)
 >      Return the intersection of two sets as a new set.
 >
 >      (i.e. all elements that are in both sets.)
 >
 >  intersection_update(...)
 >      Update a set with the intersection of itself and another.
 >
 >  isdisjoint(...)
 >      Return True if two sets have a null intersection.
 >
 >  issubset(...)
 >      Report whether another set contains this set.
 >
 >  issuperset(...)
 >      Report whether this set contains another set.
 >
 >  pop(...)
 >      Remove and return an arbitrary set element.
 >      Raises KeyError if the set is empty.
 >
 >  remove(...)
 >      Remove an element from a set; it must be a member.
 >
 >      If the element is not a member, raise a KeyError.
 >
 >  symmetric_difference(...)
 >      Return the symmetric difference of two sets as a new set.
 >
 >      (i.e. all elements that are in exactly one of the sets.)
 >
 >  symmetric_difference_update(...)
 >      Update a set with the symmetric difference of itself and another.
 >
 >  union(...)
 >      Return the union of sets as a new set.
 >
 >      (i.e. all elements that are in either set.)
 >
 >  update(...)
 >      Update a set with the union of itself and others.

---
# Python Dictionary Methods 

- clear()      :   	Removes all the elements from the dictionary
- copy()       :   	Returns a copy of the dictionary
- fromkeys()   :   	Returns a dictionary with the specified keys and value
- get()        :   	Returns the value of the specified key
- items()      :   	Returns a list containing a tuple for each key value pair
- keys()       :   	Returns a list containing the dictionary's keys
- pop()        :   	Removes the element with the specified key
- popitem()    :   	Removes the last inserted key-value pair
- setdefault() :   	Returns the value of the specified key. If the key d- oes not exist: insert the key, with the specified value
- update()     :   	Updates the dictionary with the specified key-value pairs
- values()     :   	Returns a list of all the values in the dictionary   


 >  clear(...)
 >      D.clear() -> None.  Remove all items from D.
 >
 >  copy(...)
 >      D.copy() -> a shallow copy of D
 >
 >  get(self, key, default=None, /)
 >      Return the value for key if key is in the dictionary, else default.
 >
 >  items(...)
 >      D.items() -> a set-like object providing a view on D's items
 >
 >  keys(...)
 >      D.keys() -> a set-like object providing a view on D's keys
 >
 >  pop(...)
 >      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 >
 >      If the key is not found, return the default if given; otherwise,
 >      raise a KeyError.
 >
 >  popitem(self, /)
 >      Remove and return a (key, value) pair as a 2-tuple.
 >
 >      Pairs are returned in LIFO (last-in, first-out) order.
 >      Raises KeyError if the dict is empty.
 >
 >  setdefault(self, key, default=None, /)
 >      Insert key with a value of default if key is not in the dictionary.
 >
 >      Return the value for key if key is in the dictionary, else default.
 >
 >  update(...)
 >      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 >      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 >      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 >      In either case, this is followed by: for k in F:  D[k] = F[k]
 >
 >  values(...)
 >      D.values() -> an object providing a view on D's values
 >
---

# Python String Methods 


* capitalize()   : 	Converts the first character to upper case
* casefold()     : 	Converts string into lower case
* center()       : 	Returns a centered string
* count()        : 	Returns the number of times a specified value occurs in a string
* encode()       : 	Returns an encoded version of the string
* endswith()     : 	Returns true if the string ends with the specified value
* expandtabs()   : 	Sets the tab size of the string
* find()         : 	Searches the string for a specified value and returns the position of where it was found
* format()       : 	Formats specified values in a string
* format_map()   : 	Formats specified values in a string
* index()        : 	Searches the string for a specified value and returns the position of where it was found
* isalnum()      : 	Returns True if all characters in the string are alphanumeric
* isalpha()      : 	Returns True if all characters in the string are in the alphabet
* isascii()      : 	Returns True if all characters in the string are ascii characters
* isdecimal()    : 	Returns True if all characters in the string are decimals
* isdigit()      : 	Returns True if all characters in the string are digits
* isidentifier() : 	Returns True if the string is an identifier
* islower()      : 	Returns True if all characters in the string are lower case
* isnumeric()    : 	Returns True if all characters in the string are numeric
* isprintable()  : 	Returns True if all characters in the string are printable
* isspace()      : 	Returns True if all characters in the string are whitespaces
* istitle()      : 	Returns True if the string follows the rules of a title
* isupper()      : 	Returns True if all characters in the string are upper case
* join()         : 	Converts the elements of an iterable into a string
* ljust()        : 	Returns a left justified version of the string
* lower()        : 	Converts a string into lower case
* lstrip()       :  Returns a left trim version of the string
* maketrans()    :  Returns a translation table to be used in translations
* partition()    : 	Returns a tuple where the string is parted into three parts
* replace()      : 	Returns a string where a specified value is replaced with a specified value
* rfind()        : 	Searches the string for a specified value and returns the last position of where it was found
* rindex()       : 	Searches the string for a specified value and returns the last position of where it was found
* rjust()        : 	Returns a right justified version of the string
* rpartition()   : 	Returns a tuple where the string is parted into three parts
* rsplit()       : 	Splits the string at the specified separator, and returns a list
* rstrip()       : 	Returns a right trim version of the string
* split()        : 	Splits the string at the specified separator, and returns a list
* splitlines()   : 	Splits the string at line breaks and returns a list
* startswith()   : 	Returns true if the string starts with the specified value
* strip()        : 	Returns a trimmed version of the string
* swapcase()     : 	Swaps cases, lower case becomes upper case and vice versa
* title()        : 	Converts the first character of each word to upper case
* translate()    : 	Returns a translated string
* upper()        : 	Converts a string into upper case
* zfill()        : 	Fills the string with a specified number of 0 values at the beginning  


----

## Python File Methods

* close()      :	Closes the file
* detach()     :	Returns the separated raw stream from the buffer
* fileno()     :	Returns a number that represents the stream, from the operating system's perspective
* flush()      :	Flushes the internal buffer
* isatty()     :	Returns whether the file stream is interactive or not
* read()       :	Returns the file content
* readable()   :	Returns whether the file stream can be read or not
* readline()   :	Returns one line from the file
* readlines()  :	Returns a list of lines from the file
* seek()       :	Change the file position
* seekable()   :	Returns whether the file allows us to change the file position
* tell()       :	Returns the current file position
* truncate()   :	Resizes the file to a specified size
* writable()   :	Returns whether the file can be written to or not
* write()      :	Writes the specified string to the file
* writelines() :	Writes a list of strings to the file

```
num = int(input("Enter The Number: "))
sum = 0
leng = len(str(num))
n = num
while n > 0:
    digit = n % 10
    sum += digit**leng
    n //= 10
if num == sum:
    print(num, "Is An Amstrong Number..")
else:
    print(num, "Is Not An Amstrong Number..")
```