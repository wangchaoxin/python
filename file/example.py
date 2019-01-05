# 读写文件

import json

# 1.使用with语句:自动关闭文件，不使用的话得调用f.close()
# It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is
# properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much
# shorter than writing equivalent try-finally blocks:
workfile = 'workfile'
with open(workfile) as f:
    read_data = f.read()  # read不加size  read(size) 默认读取所有行
    # print(read_data)
# print(f.closed)

# Methods of File Objects

# 2.读取一行：
# with：自动关闭文件
# To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text
#  mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative,
# the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your
# machine’s memory. Otherwise, at most size bytes are read and returned. If the end of the file has been reached,
# f.read() will return an empty string ('').
with open(workfile) as f:
    # f.read()
    while read_data:
        read_data = f.readline()
        # print(read_data, end='')
# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to
# simple code:
f = open(workfile, 'r+')
for line in f:
    print(line, end='')
f.close()

# 3.读取所有行：
#  If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
f = open(workfile, 'r+')

text = f.readlines()
print('read all lines:' + str(text))

# 4.写入数据
# f.write(string) writes the contents of string to the file, returning the number of characters written.
writeNum = f.write('This is a test\n')
print('write num:' + str(writeNum))

# 5.读写权限
# The first argument is a string containing the filename. The second argument is another string containing a few
# characters describing the way in which the file will be used. mode can be 'r' when the file will only be read,
# 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending;
# any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing.
# The mode argument is optional; 'r' will be assumed if it’s omitted.

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes
# from the beginning of the file when in binary mode and an opaque number when in text mode.
print(f.tell())

# 6.json
print(json.dumps([1, 'simple', 'list']))
# 直接dump到文件里
# Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a
# text file object opened for writing, we can do this:
json.dump('json', f)
# 从文件中读取json
f1 = open('jsonFile', 'r')
print(json.load(f1))


# 1 read files
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


f = open("jsonFile.txt", "r")
print(f.read())

# By default the read() method returns the whole text, but you can also specify how many character you want to return:
f = open("demofile.txt", "r")
print(f.read(5))

# 2 write files
# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Create a new file if it does not exist:
f = open("myfile.txt", "w")

# Delete a File
import os
os.remove("/data/a.log ")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")

# Delete Folder
os.rmdir("myfolder")