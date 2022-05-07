import csv
from fileinput import filename

filename = input("Enter the csv file to read: ")

filecontent = open(filename,"r")

csvfile = csv.DictReader(filecontent)
type(csvfile)

for line in csvfile:
    print(line)
