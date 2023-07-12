#create function that takes character ie string length 1 return true if it is vowel otherwise false.
def ganesh(vowel):
    if (vowel == 'a'or vowel== 'e' or vowel== 'i' or vowel== 'o' or vowel== 'u'):
        print("True")
    else:
        print("False")
a=ganesh("f")
def reverse(a):
    str =""
    for i in a:
        str=i+str
        return  str

a= "Ganesh"
print(reverse(a))


