# 3.1.2. Strings
# Besides numbers, Python can also manipulate strings, which can be expressed in several ways.
# They can be enclosed in single quotes ('...') or double quotes ("...") with the same result [2].
# \ can be used to escape quotes:

# \' 输出特殊字符  , \n换行
a1 = 'spam eggs'  # single quotes
print(a1)
a2 = 'doesn\'t'  # use \' to escape the single quote...
print(a2)
a3 = "\"Yes,\" they said."
print(a3)
a4 = '"Isn\'t," they said.'
print(a4)
'First line.\nSecond line.'  # 换行符

# 1.If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote:
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote,不转义字符

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 2.String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are
# automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The
# following example:   \ 在前后不分行
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3.Strings can be concatenated (glued together) with the + operator, and repeated with *:
var = 3 * 'un' + 'ium'

# 4.Strings can be indexed (subscripted), with the first character having index 0. There is no separate character
# type; a character is simply a string of size one:
word = 'Python'
var = word[0]  # character in position 0
var = word[5]  # character in position 5
# Indices may also be negative numbers, to start counting from the right:
word[-1]  # last character
word[-2]  # second-last character
# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters,
#  slicing allows you to obtain substring:
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to
# the size of the string being sliced.
word[:2]  # character from the beginning to position 2 (excluded)
word[4:]  # characters from positiuoge econd-last (included) to the end
len(word)  # 字符串长度ascii_letters

# Return a copy of the string with its first character capitalized and the  rest lowercased.
print(
    "upper size" + word.capitalize())
print("join method" + word.join(',') + word)
print("upper size" + word.capitalize())
print("word count" + str(word.count('y')))  # str()转换成字符串  count 计算出现字符个数
print("a", "b")  # a space is inserted between items, so you can format things nicely, like this:
print("a",
      end=',')  # The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string
# results in an error: If you need a different string, you should create a new one:
'J' + word[1:]  # 'Jython'
word[:2] + 'py'  # 'Pypy'

# 格式化输出
print("{0}-{1}".format("a", "b"))
# 另一种格式化方式
age_ = "%s is %d" % ('age', 18)
print(age_)
# 空值：None
a = None
if a is None:
    print(a)
if (a):
    print(a)

# 移除前后空格
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
# 字符串长度
len(a)
# 大小写
a.lower()
a.upper()
# 分割
a.split(',')
# 替换
a.replace(',', '')
