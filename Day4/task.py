#craete  one empty list and enter the list in the another list


list =[]
list1=["ABC","BCA","CAB"]
list.extend(list1)
print(list)
#create  empty list insert digit 5 to 10

list =[]
i=5
while i<=10:
    list.append(i)
   # print(i)
    i =i+1
else:
    print(list)
    print(min(list))
    print(max(list))
    #print(list.pop())
    #print(list.pop(1))
    #print(list.remove(5))
    #print(list.append(20))
    print(list)
print("End loop")

