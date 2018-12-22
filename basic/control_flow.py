a = 1
if (a):
    print("a=" + str(a))
# 1.if statement
# 获取输入
# x = int(input("Please enter an integer: "))
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# 2.for statement Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)  # insert at the firt
# 4.3. The range()
# Function The given end point is never part of the generated sequence; range(10) generates 10
# values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another
# number, or to specify a different increment (even negative; sometimes this is called the ‘step’):
for i in range(5):
    print(i)
range(5, 10)
range(0, 10, 3)  # 指定step
range(-10, -100, -30)
# To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print(range(5))  # range返回一个iterable的对象
print(list(range(5)))  # 将range转换成list

# 4.4. break and continue Statements,
#  and else Clauses on Loops Loop statements may have an else clause; it is
# executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (
# with while), but not when the loop is terminated by a break statement. This is exemplified by the following loop,
# which searches for prime numbers:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break  # 可以是continue
    else:
        # loop fell through without finding a factor,a loop’s else clause runs when no break occurs
        # 没有break的时候触发
        print(n, 'is a prime number')


# 4.5. pass Statements
#  The pass statement does nothing. It can be used when a statement is required syntactically but
#  the program requires no action. while True: pass  # Busy-wait for keyboard interrupt (Ctrl+C) This is commonly
# used for creating minimal classes:
class MyEmptyClass:
    pass


# 5.7. More on Conditions
# The conditions used in while and if statements can contain any operators,
# not just comparisons. The comparison operators in and not in check whether a value occurs (does not occur) in a
# sequence. The operators is and is not compare whether two objects are really the same object; this only matters for
#  mutable objects like lists. All comparison operators have the same priority, which is lower than that of all
# numerical operators. Comparisons can be chained. For example, a < b == c tests whether a is less than b and
# moreover b equals c. Comparisons may be combined using the Boolean operators and and or, and the outcome of a
# comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than
# comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is
# equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition. The
# Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to
# right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false,
# A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return
# value of a short-circuit operator is the last evaluated argument. It is possible to assign the result of a
# comparison or other Boolean expression to a variable. For example,
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
a, b, c = 1, 2, 3
if a > b and c > a:  # and
    print("Both conditions are True")

# 2 while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # 可以是break
    print(i)
# for loop
for x in range(6):
    print(x)  # 可以有continue和break
else:         # executed when the loop is finished
    print("Finally finished!")
