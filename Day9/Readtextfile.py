#File I/o
#Reading a file ->.read()
#Reading line by line->.readline()
my_file=open("Text file.txt",'r')
print(str(my_file.read()))
my_file.close()


print("Data line by line i text line")
my_file_line= open("Text file.txt",'r')
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
my_file_line.close()