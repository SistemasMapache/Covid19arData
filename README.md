# Covid19arData
COVID-19 Argentina data

Es repositorio es creado por Sistemas Mapache con el objetivo de poder tener un repositorio de datos abiertos de la información oficial proveniente de los partes diarios sobre la situación de COVID-19 en Argentina.

## Data


## Usar los datos

Los datos historicos provienen de fuentes oficiales y no se mezclan con fuentes no oficiales.

Para poder entender la data aquí esta el diccionario de datos:
- [Diccionario de datos](diccionariodatos.md)

### Descarga manual

[Download](https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0)

### Python

```
import pandas as pd
url = 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
df = pd.read_csv(url)
```

### R

```
library(readr)

df<-read.csv('https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0')
```


### Stata

```
import delimited using "https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0", clear
```

También estan los exports provinciales (por ahora fuente no oficial salvo Santa Fe)
- [Acceder a exports](exports/)

## Fuentes 

### Fuentes Oficiales
* Parte diario Nacional: https://www.argentina.gob.ar/coronavirus/informe-diario
* Parte diario Santa Fe: https://www.santafe.gob.ar/index.php/web/content/view/full/234420/
* Parte diario BsAs: https://www.gba.gob.ar/saludprovincia/boletin_epidemiologico
* Parte diario GCBA: https://www.buenosaires.gob.ar/salud/noticias/actualizacion-de-los-casos-coronavirus-en-la-ciudad-buenos-aires
* Parte diario Rio Negro: https://salud.rionegro.gov.ar/sala/, https://www.rionegro.gov.ar/?buscar&temas=144&catView=3
* Parte diario Misiones: https://coronavirus.misionesonline.net/
* Parte diario San Luis: http://www.sanluis.gov.ar/coronavirus/
* Parte diario Corrientes: https://www.corrientes.gob.ar/home/salud/categorias
* Parte diario Neuquen: https://www.saludneuquen.gob.ar/coronavirus-comunicados/
* Parte diario Chaco: http://comunicacion.chaco.gov.ar/lista-noticias/328
* Parte diario Tierra del fuego: https://www.facebook.com/saludtdf
* Parte diario Mendoza: http://www.salud.mendoza.gov.ar/, http://www.prensa.mendoza.gov.ar/salud/
* Parte diario Entre Rios: http://www.entrerios.gov.ar/msalud/#/ms-1/3
* Partes diarios videos oficiales Casa Rosada: https://www.youtube.com/user/casarosada/videos


### Fuentes No Oficiales 

* Datos CABA: https://eduu1993.carto.com/builder/6b400d83-bfa3-4ce1-8f3d-b680d36ce103/embed?state=%7B%22map%22%3A%7B%22ne%22%3A%5B-34.88818391007526%2C-58.98422241210938%5D%2C%22sw%22%3A%5B-34.453350878522286%2C-57.93502807617188%5D%2C%22center%22%3A%5B-34.671052719358904%2C-58.45962524414063%5D%2C%22zoom%22%3A11%7D%7D

* Datos Buenos Aires: https://public.tableau.com/profile/mart.n.dur.#!/vizhome/CasosdecoronaviruspormunicipioPBA/Hoja1?publish=yes

* Datos Rio Negro: https://public.flourish.studio/visualisation/1908120/ (https://twitter.com/ClariCardozoCas Clari Cardozo )

* Datos Cordoba (difusión): https://www.lavoz.com.ar/temas/coronavirus-en-cordoba, https://cdn.lavoz.com.ar/sites/default/files/file_attachments/nota_periodistica/PARA_PRENSA_-_29.03.2020_Informe_EPIDEMIOLOGICO_casos_confirmados.pdf

* Wiki Pandemia de enfermedad por coronavirus 2020 Argentina: https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina

* Tabla de datos diarios de Jorge Aliaga @jorgeluisaliaga: https://docs.google.com/spreadsheets/d/1M7uDgWSfy6z1MNbC9FP6jTNgvY7XchJ0m-BfW88SKtQ/edit#gid=0

* Parte diario de Nora Bär https://twitter.com/norabar

* Soporte de datos al proyecto de mapeo de OpenStreetMap: Argentina/COVID-19 https://github.com/gabriel-de-luca/covid-19 

* webgis https://covid19argentina.com/ (https://github.com/ezequiel9)


## No olvides de citarnos :)

Simplemente haciendo referencia al repositorio o si es por redes sociales usando nuestra cuenta de twitter 

> @infompaache

## Hacemos esto


### Licencia y readme

El trabajo se publica bajo licencia  Creative Commons 4.0 Internacional (CC BY 4.0).
Ver [Licencia CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) para mayor detalles.

El README fue inspirado en [*A template to make good README.md*](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)


### Ayudan en esto

Vladimiro Bellini @vlasvlasvlas

Damián Castiñeiras @damcast

Leandro Stryjek

Andres Snitcofsky @rusosnith

Telegram channel Usuaries de datos Argentina @daterxsargentina

Nadia Perez Laureda

Ezequiel Fernandez 

Dirección de estadística y censos dependiente de la subsecretaría de sistemas de tecnología de la información de la provincia de Corrientes.

Juan Cuaranta, información recoletada de Santa Fé.

Toda sugerencia es bienvenida! Tenés nuevas fuentes de partes diarios provinciales? Escriban por Issues o manden tw a @vlasvlasvlas, @damcast
