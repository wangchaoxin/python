import os

# 10.1. Operating System Interface
print("os.getcwd():", os.getcwd())  # Return the current working directory

print("os.chdir():", os.chdir('/server/accesslogs'))  # Change current working directory
print("os.mkdir():", os.system('mkdir today'))  # Run the command mkdir in the system shell
# Be sure to use the import os style instead of from os import *.
#  This will keep os.open() from shadowing the built-in open()
# function which operates much differently.

dir(os)   # 列出 模块属性

#  文件操作
# For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use
import shutil
shutil.copyfile('data.db', 'archive.db')

shutil.move('/build/executables', 'installdir')

# 10.3. Command Line Arguments
import sys
print(sys.argv)

# 10.4. Error Output Redirection and Program Termination
# The sys module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected:
sys.stderr.write('Warning, log file not found starting a new one\n')

# 10.5. String Pattern Matching

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# 10.6. Mathematics
import math
math.cos(math.pi / 4)
math.log(1024, 2)
# random
import random
random.choice(['apple', 'pear', 'banana'])

random.sample(range(100), 10)   # sampling without replacement

random.random()    # random float

random.randrange(6)    # random integer chosen from range(6)

# 10.7. Internet Access
# There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
                From: soothsayer@example.org
                
                Beware the Ides of March.
                """)
server.quit()
# 10.8. Dates and Times
# dates are easily constructed and formatted
from datetime import date
now = date.today()

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days

# 10.9. Data Compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# 10.11. Quality Control
# The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file:
import unittest
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests

