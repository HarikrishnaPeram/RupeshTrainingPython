
#Def function
def sum(n1,n2):
    print(n1+n2)
sum(45,1)
sum(1,2)
sum(22,2)


def sub(n,n2):
    print(n-n2)
sub(22,2)

def float (n1,n2):
    print(n1+n2)
sum(8,4)
float(77.1,1)

#return function
def sum_num(n1,n2):
    return n1+n2
sum1 =sum_num(2,8)
print(sum1)
sum2=sum_num(1,9)
print(sum2)
sum3=sum_num(2.1,0.9)
print(sum3)
sum4=sum_num("hari","krishna")
print(sum4)


#Global and local variables

a=10

def Scope_method():
    global a
    print(a)
def Scope_method(a):
    print(a)

def Scope_method(a):
    print(a)
    a=5
    print(a)
    return a
print(a)
#a= Scope_method()
print(a)



#try except finally blocks
try:
    x="example"
    y=1
    res=x+y
    print(age)
except NameError:
    print("error of x and y",x)
except TypeError:
    print("variable not defined:",str(y))
finally:
    print("finally block")

try:
    a=3
    b=0
    d=a//b
    print(d)
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("Thre is no exception")
finally:
    print("With in the final block")

try:
    a=7
    b="20"
    c=a//b
    print(c)
except ZeroDivisionError:
    print("ZeroDivisionError")
except TypeError:
    print("Type error")
finally:
    print("With in the final block")




