# 搜索路径
# 当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
#
# 1、当前目录
# 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
# 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
# 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
# 文件名就是module name

# import fibo.fibo

import a
from package.fibo import *  # from .. import 函数名
import sys

# If the module name is followed by as, then the name following as is bound directly to the imported module.

# import fibo as fib

# fibo.__name__  获取包名

# fibo.fibo.fib(3)
print(a.add(1, 2))
fib(3)

# 6.2. Standard Modules
# The variable sys.path is a list of strings t hat determines the interpreter’s search path for
#  modules. It is initialized to a default path taken from the environment variable PYTHONPATH, or from a built-in
# default if PYTHONPATH is not set. You can modify it using standard list operations:
# 默认python搜索路径
print(sys.path)
# The built-in function dir() is used to find out which names a module defines
print(dir(a))
# Without arguments, dir() lists the names you have defined currently:
#  it lists all types of names: variables, modules, functions, etc.
print(dir())

# Re-naming a Module
import mymodule as mx   # 改变成新名字

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1  #  引入变量

if __name__=='main':
    print("作为主函数执行")