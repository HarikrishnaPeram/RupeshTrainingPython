#predefined functions
def largest_num(*args):
    print(max(args))
largest_num(10,20,0,33,40,78,99)
def smallest_num(*args):
    print(min(args))
smallest_num(0,-2,99,22,1,3,4,55,66)

def absoult_num(a):
    print(abs(a))
absoult_num(-40)
absoult_num(50)
print(type(99))
print(type(99.88))
print(type("99"))
print(type[1,2,3,4,5])
print(type('55'))
print(type("jug"))
print(type(True))
print(type(-1))


#class and calling functions

import math
#import car

#in built constructor
class DemoMethod():
    def builten_methods(self):
        print(math.sqrt(100))
        print(math.factorial(3))
        print(math.pow(2,3))
    def car(self):
        make= '5500i'
        model = 'benz'
#        car.info(model, make)
#        car.cont(model,make)


a=DemoMethod()
a.builten_methods()
#a.car()
#car.cont(6,6)
#car.info('rst','stk')

#Defaukt constructer

class student:
    def __init__(self):
        print("call the default constructer")
        self.info="new one"
        self.findnumber="20"
    def show (self, name):
        print("name", name)
        print(self.info)
    def call(self):
        print(self.findnumber)

e= student()
e.show("Hari")
e.call()

class stud:
    count =0
    def __init__(self):
      stud.count=stud.count+1
s1=stud()
print("number of student",stud.count)
s2=stud()
print("number of student",stud.count)
s3=stud()
print("number of student",stud.count)
print()




class new:
    id= 30
    name="Hari"
    def __init__(self,name,id):
        self.id =id
        self.name=name
    def display_identity(self):
        print("id=%d\nname=%s"% (self.id,self.name))
    def new_temp(self):
        print("add new emp")
e1=new("hkk",11)
e2=new("Hari",177)
e1.display_identity()
e2.display_identity()