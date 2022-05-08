import pandas

filename = input("Enter the CSV file name to read: ")

csvfile = pandas.read_csv(filename)
print(csvfile)