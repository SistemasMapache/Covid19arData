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
yesterday = yesterday.strftime('%d/%m/%Y')

#insert por provincia
def insert (prov,casos,fallecidos):
    print(prov+' start')

    # constrain google api tope cada 10 segundos
    time.sleep(1)

    # ultima posicion para insert
    allvalues = wks1.get_all_values()
    lastrow = len(allvalues)

    # array lastval
    nextrow = lastrow+1
    
    # inserta predet
    wks1.update_cell(nextrow,  1, yesterday)
    wks1.update_cell(nextrow,  2, '=DAYS(A408;FECHA(2020;3;4))')
    wks1.update_cell(nextrow,  3, '=DAYS(A408;FECHA(2020;3;20))')
    wks1.update_cell(nextrow,  4, 'Argentina')
    
    # tot_casosconf
    wks1.update_cell(nextrow,  7, '=G'+str(lastrow)+'+H'+str(nextrow))
    
    # nue_casosconf_diff
    wks1.update_cell(nextrow,  8, casos)
    
    # tot_fallecidos
    wks1.update_cell(nextrow,  9, '=I'+str(lastrow)+'+J'+str(nextrow))
    
    # nue_fallecidos_diff
    wks1.update_cell(nextrow, 10, fallecidos)

    # formato string provs
    prov1pos = provs1.index(prov)
    wks1.update_cell(nextrow,  5, provs1[prov1pos])
    wks1.update_cell(nextrow, 18, provs2[prov1pos])
    
    print(prov+' end')
    #end

# ejemplo
# insert('Buenos Aires',5,1)