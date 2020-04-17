# needs pdftotext
# pip install requests textract pandas bs4

import requests
import textract
import re
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

# trae links
links = []
url = "https://www.argentina.gob.ar/coronavirus/informe-diario"
page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, 'html.parser')
for link in soup.findAll('a', attrs={'href': re.compile("^https://www.argentina.gob.ar/sites/default/files/")}):
    links.append(link.get('href'))

# copia pdf
url = links[0]
myfile = requests.get(url, allow_redirects=True)
open('parte.pdf', 'wb').write(myfile.content)

# extrae txt
file = 'parte.pdf'
text = textract.process(file, encoding='UTF-8',method='pdftotext')
open('parte.txt', 'wb').write(text)

# extrae casos
with open('parte.txt') as infile, open('provs.txt', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "Detalle por provincia (Nº de confirmados | Nº de acumulados)*:":
            copy = True
            continue
        elif line.strip() == "*Aquellos casos confirmados que no están notificados por residencia, fueron contabilizados":
            copy = False
            continue
        elif copy:
            line = line.replace(" | ", ",")
            line = ','.join(line.rsplit(' ', 1))
            line = line.replace('*','')
            outfile.write(line)

# TODO extrae fallecidos

# genera df
df = pd.read_csv (r'provs.txt', names=['provincia','casos_nuevos','casos_totales'])
df['fallecidos'] = 0
dfcasos = df[df.casos_nuevos > 0]

# exporta csv
dfcasos[['provincia','casos_nuevos','fallecidos']].to_csv (r'casos.csv', index = False, header=False)
