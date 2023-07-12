obj=open("C:\\Users\\sds01798\\PycharmProjects\\ RupeshTraining\\PythonBasics\\Day9\\Text file.txt",'r')
#Tell method is used the find the cursor position
print(obj.tell())
print(obj.readline())
print(obj.tell())
print(obj.readline())
print(obj.tell())
print(obj.readline())
print(obj.tell())
print(obj.readline())
#seek  method used to chage the cursor position
print(obj.tell())
print(obj.seek(10))
print(obj.tell())

