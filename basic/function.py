# 4.6. Defining Functions
def fib(n):  # write Fibonacci series up to n
    # 函数注释 The first statement of the function body can optionally be a string literal; this string literal is the
    # function’s documentation string, or docstring
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(20)
# 函数重命名： This value can be assigned to another name which can then also be used as a function. This serves as a
# general renaming mechanism:
f = fib
f(20)


def add(a, b):
    return a + b


def testList(list):
    list.append(1)
    print("test list " + str(list[0]))


list1 = []
testList(list1)
print(add(1, 2))


# 4.7.1. Default Argument Values
# The most useful form is to specify a default value for one or more arguments. This
# creates a function that can be called with fewer arguments than it is defined to allow. For example:
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        # This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# This function can be called in several ways:
# giving only the mandatory argument: ask_ok('Do you really want to quit?')
# giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
# or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# 4.7.2. Keyword Arguments