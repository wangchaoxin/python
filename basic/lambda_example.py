# 4.7.5. Lambda Expressions
# Small anonymous functions can be created with the lambda keyword. This function returns
# the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are
# required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for
#  a normal function definition. Like nested function definitions, lambda functions can reference variables from the
# containing scope:


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
f(0)
f(1)

# Another use is to pass a small function as an argument:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


x = lambda a : a + 10
print(x(5))
#  多个参数
x = lambda a, b : a * b
print(x(5, 6))


# Why Use Lambda Functions? The power of lambda is better shown when you use them as an anonymous function inside
# another function. Say you have a function definition that takes one argument, and that argument will be multiplied
# with an unknown number:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))