def function(*a):
   print(max(a))
function(1,2,3,4,56,33)

def function(*a):
   print((a))
function(1,2,3,4,56,33)

class practice:
   def car (self):
      make ='6636i'
      model ='audi'
      self.car.info= (make, model)

a=practice
#a.cont(10,10)
b=a.car=("abc","bca")
print(b)

class mass:
   def __init__(self):
      print("Default const")
      self.name= "harikrishna"
      self.age=26
   def details(self,name):
      print("name",name)

a=mass()
a.details("hari")

