# https://gspread.readthedocs.io/en/latest/
import gspread
import time
from google.oauth2.service_account import Credentials
from datetime import date, timedelta

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# keys https://gspread.readthedocs.io/en/latest/oauth2.html
credentials = Credentials.from_service_account_file('keys.json', scopes=scope)

gc = gspread.authorize(credentials)

# spreadsheet
sh = gc.open_by_key("16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA")

# historico
wks1 = sh.worksheet("historico")
wks2 = sh.worksheet("contexto")

# values provincias formatos
provs1 = wks2.col_values(2)
provs2 = wks2.col_values(3)
  
yesterday = date.today() - timedelta(days=1)
today     = date.today().strftime('%d/%m/%Y')
yesterday = yesterday.strftime('%d/%m/%Y')

fechacol1 = yesterday

#insert por provincia
def insert (prov,casos,fallecidos):
    print(prov+' strt')

    # ultima posicion para insert
    time.sleep(1)
    allvalues = wks1.get_all_values()
    lastrow = len(allvalues)

    # array lastval
    nextrow = lastrow+1
    
    # inserta predet
    time.sleep(1)
    wks1.update_cell(nextrow,  1, fechacol1)
    time.sleep(1)
    wks1.update_cell(nextrow,  2, '=DAYS(A408;FECHA(2020;3;4))')
    time.sleep(1)
    wks1.update_cell(nextrow,  3, '=DAYS(A408;FECHA(2020;3;20))')
    time.sleep(1)
    wks1.update_cell(nextrow,  4, 'Argentina')
    
    # tot_casosconf
    time.sleep(1)
    wks1.update_cell(nextrow,  7, '=G'+str(lastrow)+'+H'+str(nextrow))
    
    # nue_casosconf_diff
    time.sleep(1)
    wks1.update_cell(nextrow,  8, casos)
    
    # tot_fallecidos
    time.sleep(1)
    wks1.update_cell(nextrow,  9, '=I'+str(lastrow)+'+J'+str(nextrow))
    
    # nue_fallecidos_diff
    time.sleep(1)
    wks1.update_cell(nextrow, 10, fallecidos)

    # formato string provs
    prov1pos = provs1.index(prov)
    # post
    time.sleep(1)
    wks1.update_cell(nextrow,  5, provs1[prov1pos])
    time.sleep(1)
    wks1.update_cell(nextrow, 18, provs2[prov1pos])
    
    print(prov+' nd')
    #end

# ejemplo
# insert('Buenos Aires',3,1)
# usar casos.csv. chequear fallecidos. correr.
# ej insert('Buenos Aires', 30, 3 )

 ## 7 nuevas muertes. Todos hombres; tres de ellos, de 54, 79 y 92 años, residentes en la Provincia de Buenos Aires,
 # uno de 85 años residente en Mendoza; otros dos, de 86 y 95 años residentes en la CABA 

# extrae casos
with open('casos.csv') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    prep = line.split(",")
    print(prep)
    insert( prep[0] , int(prep[1]) , int(prep[2]) )
