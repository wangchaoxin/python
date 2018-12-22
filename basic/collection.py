# coding=utf-8
from collections import deque

squares = [1, 4, 9, 16, 25]

# Like strings (and all other built-in sequence type), lists can be indexed and sliced:
squares[0]  # indexing returns the item

# All slice operations return a new list containing the requested elements.
#  This means that the following slice returns a new (shallow) copy of the list:
squares[:]

# Lists also support operations like concatenation:
squares + [36, 49, 64, 81, 100]

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value

# You can also add new items at the end of the list, by using the append() method (we will see more about methods
# later):
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
# now remove them
letters[2:5] = []
# clear the list by replacing all the elements with an empty list
letters[:] = []

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
len(letters)
# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]

a = [1]

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
#
# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
#
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
#
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
#
# list.clear()
# Remove all items from the list. Equivalent to del a[:].
#
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
#
# list.count(x)
# Return the number of times x appears in the list.
#
# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#
# list.reverse()
# Reverse the elements of the list in place.
#
# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

print(fruits.reverse())
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
fruits

fruits.pop()
a.insert(0, 1)

# 5.1.1. Using Lists as Stacks¶ The list methods make it very easy to use a list as a stack, where the last element
# added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append().
# To retrieve an item from the top of the stack, use pop() without an explicit index. For example:
stack = [3, 4, 5, 6, 7]
stack.pop()

# 5.1.2. Using Lists as Queues It is also possible to use a list as a queue, where the first element added is the
# first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends
# and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of
# the other elements have to be shifted by one). To implement a queue, use collections.deque which was designed to
# have fast appends and pops from both ends. For example:

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
queue.popleft()  # The first to arrive now leaves

queue.popleft()  # The second to arrive now leaves

queue  # Remaining queue in order of arrival

# 5.1.3. List Comprehensions List comprehensions provide a concise way to create lists. Common applications are to
# make new lists where each element is the result of some operations applied to each member of another sequence or
# iterable, or to create a subsequence of those elements that satisfy a certain condition. For example,
# assume we want to create a list of squares, like:
squares = []
for x in range(10):
    squares.append(x ** 2)
squares = [x ** 2 for x in range(10)]  # 两个表达式相等

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x * 2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x ** 2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]
# List comprehensions can contain complex expressions and nested functions:
from math import pi

[str(round(pi, i)) for i in range(1, 6)]

# 5.2. The del statement There is a way to remove an item from a list given its index instead of its value: the del
# statement. This differs from the pop() method which returns a value. The del statement can also be used to remove
# slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For
#  example:
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]

# 5.3. Tuples and Sequences
# A tuple consists of a number of values separated by commas
t = [12345, 54321, 'hello!']
t[0]
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
# Tuples are immutable:
t[0] = 88888
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
len(t)

# 5.4. Sets
# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical
# operations like union, intersection, difference, and symmetric difference. Curly braces or the set() function can
# be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty
# dictionary, a data structure that we discuss in the next section.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
'orange' in basket                 # fast membership testing
'crabgrass' in basket
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both



