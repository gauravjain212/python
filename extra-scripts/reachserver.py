from openpyxl import load_workbook
import pandas as pd

'''
book = load_workbook("ciqip.xlsx")

sheet = book['sheet name']

for row in sheet.row:
    print(row[1].value)
'''
'''
pd.options.display.max_rows = 999

df = pd.read_excel('ciqip.xlsx')

print(df['Listener IP'])
'''

#Insert complete path to the excel file and index of the worksheet
df = pd.read_excel("ciqip.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Listener_name']) 
list2 = list(df['Listener IP'])

print(list1)
print(list2)
