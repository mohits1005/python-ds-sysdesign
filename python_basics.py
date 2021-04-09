from datetime import date

## args kwargs
'''
def func(*args, **kwargs):
    print("args:",args)
    print("kwargs:",kwargs)
func('some',1,'values',key1="apple",key2="orange")
'''
## basic oops
'''
class Test:
    stream = 'cse'

    __balance = 0

    def __init__(self, name):
        self.name = name

    def fun(self):
        print("hello, ",self.name)
    
    def getAddr(self):
        print(self.address)
    
    def setAddr(self, address):
        self.address = address
    
    def getBalance(self):
        print(self.__balance)
    
    def setBalance(self, balance):
        self.__balance = balance

obj = Test('John')
obj.fun()
print(Test.stream)
obj.setAddr("XYZ Town")
obj.getAddr()
obj.getBalance()
'''
## inheritance
'''
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        print(self.name)
    def isEmployee(self):
        print(False)

class Employee(Person):
    def isEmployee(self):
        print(True)
        

emp = Person("EMP1")
emp.getName()
emp.isEmployee()
emp2 = Employee("EMP2")
emp2.getName()
emp2.isEmployee()
print(issubclass(Employee, Person))
print(isinstance(emp, Employee))
'''
## Multiple inheritance
'''
class Base1(object):
    def __init__(self):
        self.str1 = "test1"
        print("base1")
class Base2(object):
    def __init__(self):
        self.str2 = "test2"
        print("base2")
class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("derived")
    def printstuff(self):
        print(self.str1, self.str2)
ob = Derived()
ob.printstuff()
'''
## Using Base class objects
'''
class Base(object):
    def __init__(self,x):
        self.x = x

class Derived(Base):
    def __init__(self,x,y):
        # Base.x = x
        super(Derived, self).__init__(x)
        self.y = y
    def printstuff(self):
        print(self.x,self.y)
d = Derived(10,20)
d.printstuff()
'''
## classmethod (Factory/Constructor) and staticmethod (Utlility)
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year-year)
    
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('john', 40)
print(person1.age, person1.name)
person2 = Person.fromBirthYear('doe', 1996)
print(person1.age, person1.name)
print(person2.age, person2.name)
'''
## Dunder Methods ( Magic Methods ) New Method
'''
class A(object):
    def __new__(cls,*args,**kwargs):
        print('Creating Instance')
        # return super(A, cls).__new__(cls)
        return object.__new__(cls)
    
    def __init__(self,*args,**kwargs):
        print("Init is called", args, kwargs)

a = A("test",string2="new")
'''