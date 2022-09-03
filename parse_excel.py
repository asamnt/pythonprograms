import xlrd

book = xlrd.open_workbook('./data/SOWC 2014 Stat Tables_Table 9.xls')
for sheet in book.sheets():
    print(sheet.name)
sheet = book.sheet_by_name('Table 9 ')
#print(dir(sheet))
print(sheet.nrows)