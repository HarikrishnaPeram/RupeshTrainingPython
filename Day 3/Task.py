dict={}
dict['']="String"

dict['   ']=200
print(dict)
print(dict.values())
print(dict.keys())
print(dict.items())

a = "Ganesh"

str =" "
for i in a:
    str=i+str
    str = str+i
print(str)