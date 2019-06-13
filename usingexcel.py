import openpyxl
import os
print(os.getcwd())
wb = openpyxl.load_workbook('..\\..\\..\\..\\Desktop\\example.xlsx')
print(type(wb))
print(wb.sheetnames)
sheet = wb["Sheet1"]
print(sheet)
