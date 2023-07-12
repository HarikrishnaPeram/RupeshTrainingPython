# code for even and odd number 10
def palindrome_number(a):
    new_num = a
    num=0
    while a>0:
        temp=a%10
        num = num*10+temp
        a=a//10

    if new_num==num:
        print("It is true",num)
        return True
    else:
        print("It is false",num)
        return False


find_palindrome_num= palindrome_number(121)
if find_palindrome_num==True:
    print("It is a palindrome")
else:
    print("It is not a palidrome")



