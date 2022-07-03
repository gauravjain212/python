from email.header import Header
import pandas as pd

'''
df = pd.DataFrame(pd.read_excel("test.xlsx"))

print(df)
print(type(df))
'''
'''
read_file = pd.read_excel("test.xlsx")

read_file.to_csv ("test.csv", index= None, header=True)

df = pd.DataFrame(pd.read_csv("test.csv"))

print(type(df))
print(df)
'''
# importe required libraries
import openpyxl
import csv
import pandas as pd
  
# open given workbook 
# and store in excel object 
excel = openpyxl.load_workbook("test.xlsx")
  
# select the active sheet
sheet = excel.active
  
# writer object is created
col = csv.writer(open("tt.csv",'w',newline=""))
  
# writing the data in csv file
for r in sheet.rows:
    # row by row write 
    # operation is perform
    col.writerow([cell.value for cell in r])
  
# read the csv file and 
# convert into dataframe object 
df = pd.DataFrame(pd.read_csv("tt.csv"))

# show the dataframe
print(df)