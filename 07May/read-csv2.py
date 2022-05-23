import csv

filename = input("Enter the csv file to read: ")

filecontent = open(filename,"r")

csvfile = csv.DictReader(filecontent)   #Dictinary output
print(type(csvfile))

for line in csvfile:
    print(line)
