#paramatized constructer
class student:
    def __init__(self,name):
        print("This is the pramitized constructor")
        self.name=name
    def show(self):
        print("hello",self.name)


e=student("hari")
e.show()

class calculation1:
    def summation(self,a,b):
        return a+b;
class calculation2:
    def multiplication(self,a,b):
        return a*b;
class derived (calculation1,calculation2):
    def divide (self,a,b):
        return a/b;
d=derived ()
print(issubclass(derived,calculation1))

print(issubclass(derived,calculation2))
print(issubclass(calculation1,calculation2))


#Isinstance function
class calculation1:
    def summation(self,a,b):
        return a+b;
class calculation2:
    def multiplication(self,a,b):
        return a*b;
class derived (calculation1,calculation2):
    def divide (self,a,b):
        return a/b;

d= derived()
print(isinstance(d,derived))
print(isinstance(d,calculation1))
print(isinstance(d,calculation2))
print(d.summation(12,16))
print(d.multiplication(6,7))
print(d.divide(10,2))


#inheritense
#single inheritense
class sampl1:
    def display(self):
        print("f1")
    def display1(self):
        print("f2")
class sampl2(sampl1):
    def display2(self):
        print("new display")
    def display3(self):
        print("display 2 new")
e=sampl2()
e.display()
e.display1()
e.display2()
e.display3()


#Multiple inheritense
class calculation:
    def sum(self,a,b):
        return a+b
class calculation1:
    def multiple(self,a,b):
        return a*b
class calculation2:
    def sub(self,a,b):
        return a-b
class derived (calculation,calculation1,calculation2):
    def divide(self,a,b):
        return a/b
d=derived()
print(d.sum(40,20))
print(d.sub(40,20))
print(d.divide(10,10))
print(d.multiple(10,10))
#multi level inhertense
class sample:
    def define(self):
        print("new email")
class sample1(sample):
    def define1(self):
        print("new mail2")
class sample3(sample1):
    def define2(self):
        print("main class")
e=sample3()
e.define()
e.define2()
e.define1()
#ploymorphism
#1 method overloading and 2 method over riding
#1 method overloading  "same method name but different argument not supporting in python
#2. method over riding  method overriding from parent to child
#Over riding
class Bank():
    def getinst(self):
        return 10
class sbi(Bank):
    def getinst(self):
        return 9
class icici():
    def getinst(self):
        return 8

b1=Bank()
b2=sbi()
b3=icici()
print("Bank interest",b1.getinst())
print("Bank interest",b2.getinst())
print("Bank interest",b3.getinst())

#Hierarchical_inheritance:
class parent:
    def fun1(self):
        print("This is the parent")
class child1(parent):
    def fun2 (self):
        print("This is the first child")

class child2(parent):
    def fun3(self):
        print("This is the second child")
b=child1()
b1=child2()
b.fun1()
#b1.fun2()
b.fun1()
b1.fun3()

