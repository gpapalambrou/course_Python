# some class examples

class Cal(object):
    """Cal class definition"""
    # pi is a class variable
    pi = 3.142

    def __init__(self, radius):
        # self.radius is an instance variable
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)


class MyClass(object):
    'MyClass class definition'
    myVersion = '1.1'           # static data
    def showMyVersion(self):    # method
        print('MyClass.myVersion')


# 13.1 Wesley Chun
class P(object):
    pass

class C(P):
    pass



""" Some echo to command line """
# select code + right-click -> "execute selection in console"
a = Cal(32)
a.area()
# Output: 3217.408

a.pi
# Output: 3.142

a.pi = 43
a.pi
# Output: 43

b = Cal(44)
b.area()
# Output: 6082.912

b.pi
# Output: 3.142

b.pi = 50
b.pi
# Output: 50

""" Below some codes for finding class attributes """

dir(Cal)        # dir() shows Class Attributes

Cal.__dict__    #__dict__ shows Class Attributes

Cal.__name__

Cal.__doc__


mc = MyClass()
dir(MyClass)
MyClass.__doc__

c=C()
c.__class__
C.__bases__