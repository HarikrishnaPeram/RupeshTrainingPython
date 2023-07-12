# list
list=[1,11,12,3,4,6,0,8,22,34,56,77]
print(min(list))
print(max(list))
#print(list.index(9))
print(list.pop()) #pop = print last value in the list (int)
print(list.pop(1))
print(list)
del list[2]
list.remove(0)
print(list)
print(list.copy())
print(list.clear())


# Take  list of number and print the num
num=[1,2,3]
i=0
sum=0
while i<=2:
    sum = sum+num[i]
    i+=1
print(sum)
#append  " To update values in the list at last"
#insert aare used to insert the values 1st index (1, insert)
#extend " it will come


list=["abd","aca","aca","ava","ava"]
list.insert(1,"aaaa")
print(list)
list1=["gag","agfa","aga"]
list.extend(list1)
print(list)


#creating list from the empty list
l =[]
num =0
while(num<10):
    l.append(num)
    print(num)
    num=num+1
else:
    print(l)



