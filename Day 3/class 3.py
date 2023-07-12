#nested if condition
x= int(input("enter value of x:"))
if x>10:
    print("Above 10")
    if x>50:
        print("Above 50")
    else:
        print("less than 50")
else:
    print("x is below 10")

#While else break and continue
x=0
while(x<10):
    print(x)
    x=x+1
    if (x==8):
        continue
    print("this is assume")
else:
    print("end loop")

# for loop
num=[2,3,4,7,9]
sum=0
for i in num:
    sum=sum+i
print(sum)

#range function
for i in range(5):
    print(i)
else:
    print("fin")
for x in range(2,30,2):
    print(x)


#dictnory
car= {"name":'honda',"model":"tiago","year":2021}
print(car)
model =car["model"]
print(model)
d={}
d["one"]=1
d["two"]= 2
print(d)
sum1= d['two']+8
print(sum1)


car= {"makes":"bmw","model":"2200","year":2021}
cars= {"benz":{"makes":"benz","model":"2200i","year":2016},"audi":{"makes":"audi","model":"2200i","year":2021}}
print(car.keys())
print(car.values())
print(cars.keys())
print(cars.values())
print(car.items())
print(cars.items())


benz_year=cars["benz"]["year"]
print(benz_year)
print(cars["benz"]["model"])



