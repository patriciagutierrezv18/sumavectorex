import xlwt
import random

def crear_archivo():
    vector=[]
    vector_uno=[]
    vector_dos=[]
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('vector')
    
    for i in range(2):
        for j in range(6):
            na = random.randint(0,20)
            ws.write(i,j,na)

    ws.write(3,0,xlwt.Formula("A1+A2"))
    ws.write(3,1,xlwt.Formula("B1+B2"))
    ws.write(3,2,xlwt.Formula("C1+C2"))
    ws.write(3,3,xlwt.Formula("D1+D2"))
    ws.write(3,4,xlwt.Formula("E1+E2"))
    ws.write(3,5,xlwt.Formula("F1+F2"))

    wb.save('vector excel.xls')
    print ("Archivo Generado...")
crear_archivo()
