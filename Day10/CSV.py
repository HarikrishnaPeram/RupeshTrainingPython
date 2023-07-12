import csv
f= open("C:/Users/sds01798/PycharmProjects/RupeshTraining/PythonBasics/Day10/Practice.csv")
#csv rendered file
csv_data=csv.reader(f)
list1=list(csv_data)
print(list1)
for row in list1:
    l=len(row)
    for j in range(0,1):
        print(row[j])
        f.close()