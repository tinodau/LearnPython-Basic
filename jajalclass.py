# OBJECT
class Employee :
    "Coba coba bikin class"

    empCount = 0

    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount (self) :
        print ("Total Employee %d", Employee.empCount)

    def displayEmployee (self) :
        print ("Name : ", self.name , ", salary : ", self.salary)

emp1 = Employee("Tino", 100000000)
emp2 = Employee("Daulat", 200000000)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total employee : %d" % Employee.empCount)
print ("\n\n")

#=========================================
# INHERITANCE
# adopt function

class Parent :
    parentAttr = 100
    def __init__(self) :
        print ("Calling parent Constructor")

    def parentMethod(self) :
        print ("Calling parent Method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribut : ", Parent.parentAttr)

class Child(Parent) :
    def __init__ (self):
        print ("Calling Child Constructor")

    def childMethod(self):
        print ("Calling Child Method")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print ("\n\n")


# ==============================================
# OVERRIDING
# rewrite method

class Parent2:
    def myMethod(self):
        print ("Calling Parent Method")


class Child2(Parent2):
    """docstring for Child2."""
    def myMethod(self):
        print("Calling Child2 Method")

c2 = Child2()
c2.myMethod()

print ("\n\n")


# ====================================================
# OVERLOADING
# same method, diff parameter

class Vektor:
    """docstring for Vektor."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vektor (%d, %d)' % (self.a, self.b)

    def __add__(self, other): #overload __str__
        return Vektor (self.a + other.a, self.b + other.b)

v1 = Vektor(10,1)
v2 = Vektor(5,1)

print(v1 + v2)
print ("\n\n")


# ====================================================
# MODIFIER
# data hiding

class JustCounter :
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print (counter.__secretCount) # will show error
print (counter._JustCounter__secretCount)
