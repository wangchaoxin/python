# 5.5. Dictionaries Another useful data type built into Python is the dictionary (see Mapping Types — dict).
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike
# sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable
# type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers,
# or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You
# can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments,
# or methods like append() and extend(). It is best to think of a dictionary as a set of key: value pairs,
# with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty
# dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to
#  the dictionary; this is also the way dictionaries are written on output. The main operations on a dictionary are
# storing a value with some key and extracting the value given the key. It is also possible to delete a key:value
# pair with del. If you store using a key that is already in use, the old value associated with that key is
# forgotten. It is an error to extract a value using a non-existent key. Performing list(d) on a dictionary returns a
#  list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d)
# instead). To check whether a single key is in the dictionary, use the in keyword.
import math

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127  # put操作
tel

tel['jack']

del tel['sape']  # 删除key
tel['irv'] = 4127
tel

list(tel)  # key的list

sorted(tel)  # key的list 按照插入顺序

'guido' in tel

'jack' not in tel

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x ** 2 for x in (2, 4, 6)}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)

# 5.6. Looping Techniques When looping through dictionaries, the key and corresponding value can be retrieved at the
# same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using
#  the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 反转集合：To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the
# reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)
# 集合排序：  To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while
# leaving the source unaltered.

# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data
