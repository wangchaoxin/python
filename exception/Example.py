import sys

# 10 / 0
try:
    10 / 0
except BaseException as e:  # 所有异常的基类
    # except (RuntimeError, TypeError, NameError):  # 定义多个异常
    print('exception happens:' + str(e))  # 打印异常
    print("Unexpected error:", sys.exc_info()[0])
    raise  # 抛出异常

# The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution,
# since it is easy to mask a real programming error in this way! It can also be used to print an error message and
# then re-raise the exception (allowing a caller to handle the exception as well):
except:  # 匹配其余异常
    print("Unexpected error:", sys.exc_info()[0])
    pass
# The try … except statement has an optional else clause, which, when present, must follow all except clauses.
# It is useful for code that must be executed if the try clause does not raise an exception. For example:
else:  # 最终执行的语句
    print("finally execute")

# The except clause may specify a variable after the exception name. The variable is bound to an exception instance
#  with the arguments stored in instance.args. For convenience, the exception instance defines __str__() so the arguments
#  can be printed directly without having to reference .args. One may also instantiate an exception first before raising
# it and add any attributes to it as desired.
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)


# 2.抛出异常
# raise NameError('name error')
# raise ValueError  # shorthand for 'raise ValueError()'  默认调用无参构造函数

#  自定义异常

# Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes).
#  Exceptions should typically be derived from the Exception class, either directly or indirectly.
# Exception classes can be defined which do anything any other class can do, but are usually kept simple,
#  often only offering a number of attributes that allow information about the error to be extracted by handlers
# for the exception. When creating a module that can raise several distinct errors, a common practice is to create
# a base class for exceptions defined by that module, and subclass that to create specific exception classes for different
# error conditions:

class Error(Exception):  # 继承基类异常
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
# finally语句
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# 8.7. Predefined Clean-up Actions
# Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether
#  or not the operation using the object succeeded or failed. Look at the following example, which tries to open a file and
# print its contents to the screen.
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")