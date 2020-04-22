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
        if line.strip().startswith('Detalle por provincia'):
            copy = True
            continue
        elif line.strip().startswith('*Aquellos casos confirmados que no están notificados por residencia'):
            copy = False
            continue
        elif copy:
            if str(line) != '':
                line = line.replace(" / ", ",")
                line = ','.join(line.rsplit(' ', 1))
                line = line.replace('*','')
                line = line.replace('Ciudad de Buenos Aires','CABA')
                outfile.write(str(line))

# TODO : extrae fallecidos, join df fallecidos where prov = prov # NLP NLTK
# fallecidos

# extrae casos
with open('parte.txt') as infile, open('fallecidos.txt', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip().startswith('Se registraron'):
            copy = True
            outfile.write(str(line))
            continue
        elif line.strip().startswith("Del total de casos"):
            copy = False
            continue
        elif line.strip().startswith("A la fecha"):
            copy = False
            continue
        elif line.strip().startswith("Detalle por provincia"):
            copy = False
            continue
        elif copy:
            if str(line) != '':
                outfile.write(str(line))


# genera df
df = pd.read_csv (r'provs.txt', names=['provincia','casos_nuevos','casos_totales'])
# add col
df['fallecidos'] = 0
dfcasos = df[df.casos_nuevos > 0]
# dfcasos = df[df.astype(int)]
# exporta csv
dfcasos = dfcasos.dropna(subset=['casos_nuevos'])
# decimals
m=(dfcasos.dtypes=='float')
dfcasos.loc[:,m]=dfcasos.loc[:,m].astype(int)

dfcasos[['provincia','casos_nuevos','fallecidos']].to_csv (r'casos.csv', index = False, header=False)

# extrae casos
with open('casos.csv') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    prep = line.split(",")
    print(prep)
#check ok
