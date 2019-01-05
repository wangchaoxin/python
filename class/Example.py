class MyClass:
    """A simple example class"""

    # 全局变量 ，通过MyClass.i and MyClass.f，可以进行赋值 MyClass.i=2
    i = 12345

    def f(self):
        return 'hello world'

    # 构造函数
    def __init__(self):
        print('constructor')
        self.data = [1]

    #  带参数构造函数
    # def __init__(self, realpart, imagpart):
    #     self.r = realpart
    #     self.i = imagpart


# 2.Class and Instance Variables
class Dog:
    kind = 'canine'  # class variable shared by all instances,所有实例共享

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance，每个实例特有的
        self.tricks = []  # 每个实例定义容器，不应该是静态变量，creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    def hello(self):
        print("parent hello")


# 一个文件里还可以单独定义函数
def test():
    print("test")


# 3.继承,
class ADog(Dog):
    # 子类默认会覆盖父类方法，通过super()调用父类方法
    def __init__(self, name):
        # Dog.__init__(name)    调用父类方法
        super().__init__(name)
        self.add_trick(1)  # 调用父类方法,通过类名调用

    def test(self):
        self.add_trick(1)  # 调用父类方法，通过实例调用


dog = ADog('ADog')
dog.hello()
# 可以将函数赋值给变量
b = test
b()

# 实例调用函数和变量
x = MyClass()
print("x.f():", x.f())
print("x.data:", x.data)

# 查看实例是否属于某一类，isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
print("is instance:", isinstance(x, MyClass))
# 查看子类是否是父类
print("is subclass:", issubclass(ADog, Dog))

print("get class:" + str(x.__class__))

print("myClass.f():", MyClass.f(x))  # MyClass.f(x)和x.f是等价的

a = [1, 2, 3]
b = ['a', 'b', 'c']
# zip 组成元组
for x in zip(a, b):
    print(x)
print("zip:" + str(zip(a, b)))
print(a)


# y = MyClass(1, 2)
# print(y.r, y.i)
#
# y.name='wang' #声明属性
# del y.name   # 删除属性

# 4.多继承
class A:
    def __init__(self):
        pass

    __age = 1  # 私有变量
    _name = "haha"  # protected变量

    # 私有函数
    def __privateMethod(self):
        pass


class B:
    def __init__(self):
        pass


class C(A, B):
    pass
