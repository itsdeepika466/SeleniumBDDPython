import openpyxl

file = "C:/Users/10708565/OneDrive - LTIMindtree/Documents/Data2.xlsx"
workbook=openpyxl.load_workbook(file)
sheet=workbook["Data1"]
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="welcome"
workbook.save(file)