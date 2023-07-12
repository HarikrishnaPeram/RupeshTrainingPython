# print duplicate values in the string

str =input("Enter a string")
for i in str:
    duplicate=str.count(i)
    str.count(i)

    print(i,duplicate)

def factorial(n):
   fact=1
   for i in range(2,int(n+1)):
    fact=fact*i
   print("factorial of a ",fact)
f=factorial(5)

def duplicate(a):
    for i in range(0,len(a)):
        for j  in range(i+1,len(a)):
            if (a[i]==a[j]):
                print("duplicate ", a[i])
                break
d= duplicate("Harikrishna")


def duplicate(input):
    x=[]
    for i in input:
        if i not in x   and input.count(i)>1:
            x.append(i)
    print("".join(x))
d = duplicate("Harikrishna")


class Function():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        if a>b:
            print("A is greater than B")
        else:
            print("B is greater than A")
p1=Function(5,6)







































































































