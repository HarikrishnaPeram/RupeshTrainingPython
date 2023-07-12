# Boolean
# Replacement for string %s and int %d
# conditinal statements if else elif.

# Boolean
#------------------------------------------------------------------------------------------------
a =True
b = False
c= ""
print(bool(c))
print(type(a))
print(a)
print(b)
z=b-a
print(type(z))
print(z)
print(bool(z))

# % = mod
a=2+3+4
print(a)
b=2*3+5-6
print(b)
c= (7+8)+3-1
print(c)
d= 3*4+7+3%3
print(d)
e=3*4+6-1+(10-100)
print(e)
# Index, length of string, upper and lower
#------------------------------------------------------------------------------------------------------------------
c="need a \"pen\" and \"book\""
print(c)
city = "hyderabad"
state="Telengana"
print(state+city)
print(city[0])
print(state[6])
print(city.upper())
print(state.lower())
print(len(city))
print(len(state))
print(len(city)+len(state))
print('hello'+''+'cheat')

# Replace
#------------------------------------------------
Husbend= 'rahul'
wife= 'taniya'
r ='raju'
a=8
b=9
print(Husbend+''+'thinks he is smarter than'+'+wife')
print(Husbend+'thinks he is smarter than'+wife)
print('%s thinks he is %s smarter than than %s'%(wife,r,wife))
print('"%s" thinks he is smarter than "%s"'%(Husbend,wife))
print('%d b is greater than a %s' %(a,wife))

# if else elif
#----------------------------------------------------------------------

a = int(input("Enter the value a"))
b=  int(input("Enter the value b"))
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")

a = int(input("Enter the value a"))
b=  int(input("Enter the value b"))
if a>b:
    print("a is greater than b")
elif(a==b):
    print("a is equal to b")
else:
    print("a is lessthan b")