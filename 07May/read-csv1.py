import csv

filename = input("Emnter CSV File name to read: ")

filecontent = open(filename,"r")

csvfile = csv.reader(filecontent)

for line in csvfile:
    print(line)

filecontent.close()
