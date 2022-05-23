import csv

filename = input("Emnter CSV File name to read: ") #File name want to read

filecontent = open(filename,"r")    #Open the file name 

csvfile = csv.reader(filecontent)   #Read the CSV file 

for line in csvfile:
    print(line)

filecontent.close()
