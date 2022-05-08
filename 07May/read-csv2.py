import csv

filename = input("Enter the csv file to read: ")

filecontent = open(filename,"r")

csvfile = csv.DictReader(filecontent)
print(type(csvfile))

for line in csvfile:
    print(line)
