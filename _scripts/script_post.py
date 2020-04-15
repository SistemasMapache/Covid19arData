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

# historico
wks1 = gc.open_by_key("16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA").sheet1

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

    # formato para covid19argentina.com    
    if prov == 'Buenos Aires':
        wks1.update_cell(nextrow,  5, 'Buenos Aires')
        wks1.update_cell(nextrow, 18, 'buenos-aires')

    if prov == 'Catamarca':
        wks1.update_cell(nextrow,  5, 'Catamarca')
        wks1.update_cell(nextrow, 18, 'catamarca')

    if prov == 'Chaco':
        wks1.update_cell(nextrow,  5, 'Chaco')
        wks1.update_cell(nextrow, 18, 'chaco')
	
    if prov == 'Chubut':
        wks1.update_cell(nextrow,  5, 'Chubut')
        wks1.update_cell(nextrow, 18, 'chubut')
	
    if prov == 'Ciudad de Buenos Aires':
        wks1.update_cell(nextrow,  5, 'CABA')
        wks1.update_cell(nextrow, 18, 'capital-federal')

    if prov == 'Córdoba':
        wks1.update_cell(nextrow,  5, 'Córdoba')
        wks1.update_cell(nextrow, 18, 'cordoba')
	
    if prov == 'Corrientes':
        wks1.update_cell(nextrow,  5, 'Corrientes')
        wks1.update_cell(nextrow, 18, 'corrientes')

    if prov == 'Entre Ríos':
        wks1.update_cell(nextrow,  5, 'Entre Ríos')
        wks1.update_cell(nextrow, 18, 'entre-rios')

    if prov == 'Formosa':
        wks1.update_cell(nextrow,  5, 'Formosa')
        wks1.update_cell(nextrow, 18, 'formosa')

    if prov == 'Jujuy':
        wks1.update_cell(nextrow,  5, 'Jujuy')
        wks1.update_cell(nextrow, 18, 'jujuy')

    if prov == 'La Pampa':
        wks1.update_cell(nextrow,  5, 'La Pampa')
        wks1.update_cell(nextrow, 18, 'la-pampa')
	
    if prov == 'La Rioja':
        wks1.update_cell(nextrow,  5, 'La Rioja')
        wks1.update_cell(nextrow, 18, 'la-rioja')
	
    if prov == 'Mendoza':
        wks1.update_cell(nextrow,  5, 'Mendoza')
        wks1.update_cell(nextrow, 18, 'mendoza')
	
    if prov == 'Misiones':
        wks1.update_cell(nextrow,  5, 'Misiones')
        wks1.update_cell(nextrow, 18, 'misiones')
	
    if prov == 'Neuquén':
        wks1.update_cell(nextrow,  5, 'Neuquén')
        wks1.update_cell(nextrow, 18, 'neuquen')
	
    if prov == 'Río Negro':
        wks1.update_cell(nextrow,  5, 'Río Negro')
        wks1.update_cell(nextrow, 18, 'rio-negro')
	
    if prov == 'Salta':
        wks1.update_cell(nextrow,  5, 'Salta')
        wks1.update_cell(nextrow, 18, 'salta')
	
    if prov == 'San Juan':
        wks1.update_cell(nextrow,  5, 'San Juan')
        wks1.update_cell(nextrow, 18, 'san-juan')
	
    if prov == 'San Luis':
        wks1.update_cell(nextrow,  5, 'San Luis')
        wks1.update_cell(nextrow, 18, 'san-luis')
	
    if prov == 'Santa Cruz':
        wks1.update_cell(nextrow,  5, 'Santa Cruz')
        wks1.update_cell(nextrow, 18, 'santa-cruz')
	
    if prov == 'Santa Fe':
        wks1.update_cell(nextrow,  5, 'Santa Fe')
        wks1.update_cell(nextrow, 18, 'santa-fe')

    if prov == 'Santiago del Estero':
        wks1.update_cell(nextrow,  5, 'Santiago del Estero')
        wks1.update_cell(nextrow, 18, 'santiago-del-estero')

    if prov == 'Tierra del Fuego':
        wks1.update_cell(nextrow,  5, 'Tierra del Fuego')
        wks1.update_cell(nextrow, 18, 'tierra-del-fuego')
	
    if prov == 'Tucumán':
        wks1.update_cell(nextrow,  5, 'Tucumán')
        wks1.update_cell(nextrow, 18, 'tucuman')
	
    if prov == 'Indeterminado':
        wks1.update_cell(nextrow,  5, 'Indeterminado')
        wks1.update_cell(nextrow, 18, 'no-data')
    
    print(prov+' end')
    #end

