a= "Hello"
print(a)

#create function max   that takes two arguments and returns ax value .use if else statements.
def max(a,b):
    if a>=b:
        return a
    else:
        return b
a=input("enter value of a")
b=input("enter value of b")
print(max (a,b))

#create a function max_of_three that takes  three numbers as arguments  and return  largest of them

def max_of_three (a,b,c):
   if (a>b  and a>c):
       return a
   elif b>c:
       return b
   else:
       return c
a=max_of_three(2,3,4)

print("max_of_three",a)




# create function that computes the length of given list or string
a = "Harikrishna"
print(len(a))


def list_length(a):
    return a

b=list_length(len("harikrishna"))
print(b)

#define reverse() function that comutes the reversal of string



def reverse(a):
    str =""
    for i in a:
        str=i+str
        return  str

a= "Ganesh"
print(reverse(a))




