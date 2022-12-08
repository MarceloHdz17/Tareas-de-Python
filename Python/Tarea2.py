import xlrd

filePath = "C:\\Users\\Tarea2\\TablaPosiciones.xlsx"

openFile = xlrd.open_workbook(filePath)

sheet = openFile.sheet_by_name("Hoja1")

for i in range(sheet.nrows):
    print(sheet.cell_value(i,0), "   ", sheet.cell_value(i,1))