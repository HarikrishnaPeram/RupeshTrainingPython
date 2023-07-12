import csv
f =open("Write_Prcatice.csv",'w',newline='')
csv_data= csv.writer(f)
csv_data.writerow(['hello,11,22,33'])
csv_data.writerow(['hello,11,45,67,66'])
csv_data.writerow(['hello',87,96,98])
f.close()