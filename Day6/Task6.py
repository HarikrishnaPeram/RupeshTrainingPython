# code for even and odd number 10
#num=int(input("enter number of a"))
n=10
a=n % 2
if a>0:
    print("odd number")
else:
    print("even number")



# primenumber 7
a=15
b=2
c=a % b
if c==1:
    print("It is a prime number")
else:
    print("It is a not prime number")

def prime(num):
    temp=0
    for i in range (2, int(num/2)):
        if (num%i==0):
            print(num,"is not prime number")
    else:
        print(num, "is  prime number")
b= prime(15)

def function(a,b):

    return a,b
print(a+b)
(a, b) = (6, 3)

n=1
while n<5:
    print("Harikrishna")
    n=n+1
    if n==3:
     continue

