# Covid19arData

COVID-19 Argentina data

Repositorio creado por Sistemas Mapache con el objetivo de poder contar con __datos abiertos__ de la información oficial proveniente de los partes diarios sobre la situación de COVID-19 en Argentina.

También se suman datos con mayor segmentación territorial de fuentes provinciales.

## Data

Los datos históricos provienen de fuentes oficiales y no se mezclan con fuentes no oficiales.

### Descarga y uso de datos

Es posible [__Descargar el CSV de datos históricos Oficiales (link)__](https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0) como también es posible [__acceder a la Hoja de cálculos online (link)__](https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/edit?usp=sharing)

Para poder entender la data [desde aquí puede acceder al Diccionario de datos](diccionariodatos.md).

### Usando Python

```
import pandas as pd
url = 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
df = pd.read_csv(url)
```

### Usando R

```
library(readr)

df<-read_csv('https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0')

```

### Usando Stata

```
import delimited using "https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0", clear
```

### Descarga de tablas provinciales

También están disponibles los [Exports de data provincial](exports/) que contemplan mayor segmentación territorial por provincia.


## Fuentes 

### Fuentes Oficiales

* [Parte diario Nacional](https://www.argentina.gob.ar/coronavirus/informe-diario)
* [Parte diario Santa Fe](https://www.santafe.gob.ar/index.php/web/content/view/full/234420/) y [datos abiertos Santa Fe](https://www.santafe.gob.ar/ms/covid19/datosabiertos/)
* [Parte diario BsAs](https://www.gba.gob.ar/saludprovincia/boletin_epidemiologico)
* [Parte diario GCBA](https://www.buenosaires.gob.ar/salud/noticias/actualizacion-de-los-casos-coronavirus-en-la-ciudad-buenos-aires)
* [Parte diario Rio Negro](https://www.rionegro.gov.ar/index.php?catID=17)
* [Parte diario Misiones](https://coronavirus.misionesonline.net/)
* [Parte diario San Luis](http://www.sanluis.gov.ar/coronavirus/)
* [Parte diario Corrientes](https://www.corrientes.gob.ar/home/salud/categorias)
* [Parte diario Neuquén](https://www.neuqueninforma.gob.ar/tag/parte/)
* [Parte diario Chaco](http://comunicacion.chaco.gov.ar/lista-noticias/328)
* [Parte diario Tierra del Fuego](https://www.facebook.com/saludtdf)
* [Parte diario Mendoza](http://www.prensa.mendoza.gov.ar/salud/)
* [Parte diario Entre Ríos](http://www.entrerios.gov.ar/msalud/#/ms-1/3)
* [Partes diarios videos oficiales Casa Rosada](https://www.youtube.com/user/casarosada/videos)
* [Partes diarios Córdoba](https://www.cba.gov.ar/informe-diario-de-casos-y-medidas/)
* [Parte Santa Cruz](http://saludsantacruz.gob.ar/portal/coronavirus/)


### Fuentes No Oficiales 

* Rodrigo Maidana @Rodri_LP y reporte Provincia de Buenos Aires: https://es.scribd.com/document/458561269/Informe-COVID-19-Provincia-Bs-As

* Datos CABA de mapa abierto de Eduardo Mejias: https://eduu1993.carto.com/builder/6b400d83-bfa3-4ce1-8f3d-b680d36ce103/embed?state=%7B%22map%22%3A%7B%22ne%22%3A%5B-34.88818391007526%2C-58.98422241210938%5D%2C%22sw%22%3A%5B-34.453350878522286%2C-57.93502807617188%5D%2C%22center%22%3A%5B-34.671052719358904%2C-58.45962524414063%5D%2C%22zoom%22%3A11%7D%7D

* Datos Rio Negro: https://public.flourish.studio/visualisation/1908120/ (https://twitter.com/ClariCardozoCas Clari Cardozo )

* Datos Córdoba (difusión): https://www.lavoz.com.ar/temas/coronavirus-en-cordoba, https://cdn.lavoz.com.ar/sites/default/files/file_attachments/nota_periodistica/PARA_PRENSA_-_29.03.2020_Informe_EPIDEMIOLOGICO_casos_confirmados.pdf

* Wiki Pandemia de enfermedad por coronavirus 2020 Argentina: https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina

* Tabla de datos diarios de Jorge Aliaga @jorgeluisaliaga: https://docs.google.com/spreadsheets/d/1M7uDgWSfy6z1MNbC9FP6jTNgvY7XchJ0m-BfW88SKtQ/edit#gid=0

* Parte diario de Nora Bär https://twitter.com/norabar

* Soporte de datos al proyecto de mapeo de OpenStreetMap: Argentina/COVID-19 https://github.com/gabriel-de-luca/covid-19 

* webgis https://covid19argentina.com/ (https://github.com/ezequiel9)

* dataviz pública en flourish de serie de fallecidos https://public.flourish.studio/visualisation/1695917/embed

* Export a CSV de parte oficial Santa Fe generado por Mariano Crosetti https://raw.githubusercontent.com/mariano22/argcovidapi/master/csvs/SantaFe_AllData.csv

* Argentina and Santa Fe COVID API https://github.com/mariano22/argcovidapi 
    Mariano Crosetti | Computer Sciences student @ Facebook | LinkedIn | Twitter | Github
    Juan Hernandez Ruiz | Civil Engineer Student @ Facebook | LinkedIn | Twitter

* Avance COVID Juan Quaranta Santa Fe https://docs.google.com/spreadsheets/d/1acPZ1FBtifqgZta4WeiR5aZrV3Q0g4HANPA7Edu0dos

* Casos Córdoba https://public.flourish.studio/visualisation/1692366/embed#amp=1

* Casos Neuquén y Rio Negro https://docs.google.com/spreadsheets/d/1t02E2YcKFeAt3gw09qNLJmblTyCf7mzbQkKYQulbexY/edit#gid=0

* Avance COVID Localidades Santafecinas y Argentina https://docs.google.com/spreadsheets/d/1acPZ1FBtifqgZta4WeiR5aZrV3Q0g4HANPA7Edu0dos/edit#gid=0

* Análisis COVID Grupo de Investigación en Bases de Datos - UTN - FRCU  https://github.com/GIBD/covid/tree/master/data

## Licencia y readme

El trabajo se publica bajo licencia  Creative Commons 4.0 Internacional (CC BY 4.0).
Ver [Licencia CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) para mayor detalles.

El README fue inspirado en [*A template to make good README.md*](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) y en [*el readme del dashboard BID*](https://github.com/EL-BID/IDB-IDB-Invest-Coronavirus-Impact-Dashboard)


## Quienes somos

[__Sistemas Mapache__](https://smapache.com.ar/es/) es una empresa de tecnología especializada en brindar soluciones geoespaciales web a través de herramientas FOSS.

Somos Vladimiro Bellini [@vlasvlasvlas](https://twitter.com/vlasvlasvlas), Damián Castiñeiras [@damcasti](https://twitter.com/damcasti/) y Leandro Stryjek.


## Quiénes son reutilizadores de los datos recolectados

* Grupo de Investigación en Bases de Datos - UTN - FRCU
* GCBA, Centro de Monitoreo de Incidente
* La Nación
* América 24
* Geoportal COVID19 (https://covid19argentina.com/)
* Asociación médicos Buenos Aires AMGBA (http://amgba.org.ar/amgba/covid19)
* El gato y la caja https://beta.elgatoylacaja.ar/coronavirus
* Juan Andres Fraire (CONICET) https://twitter.com/totinfraire
* Emmanuel Larussi (CONICET) https://twitter.com/emmaiarussi
* centros de datos municipales en Salta y Provincia de Buenos Aires
* Juan Francisco González Valle López (INTI)
* Repositorio no oficial de datos públicos abiertos de la República Argentina http://datar.info/
* Lavih Abraham (economista en Mirador de Actualidad del Trabajo y la Economía) https://twitter.com/lavih7
* Ariel Aizemberg (profesor ITBA en Diplomatura en Big Data y Ciencia de Datos)
* Rodrigo Maidana @Rodri_LP
* Andrés Babino,  Postdoctoral Associate at The Rockefeller University https://github.com/ababino
* Sergio Villordo PhD in Biological Chemistry and Bioinformatics Universidad de Buenos Aires (UBA), @Ser08
* Tim Riffe COVID-19 cases and deaths by age and sex https://github.com/timriffe/covid_age

## Quiénes ayudan con corrección, recolección y difusión

Diario Página 12: https://www.pagina12.com.ar/262731-coronavirus-ciudad-por-ciudad-el-mapa-interactivo-de-argenti

Diario El Litoral

Infobae

Juan Cuaranta, información recoletada de Santa Fé.

Clari Cardozo Castro (Bioquímica Epidemióloga UNC) @ClariCardozoCas

Rodrigo Maidana @Rodri_LP

Andrés Snitcofsky [@rusosnith](https://twitter.com/rusosnith)

Telegram channel Usuaries de datos Argentina @daterxsargentina

Nadia Perez Laureda

Ezequiel Fernández 

Soledad Retamar

[@ivanchowilliams](https://twitter.com/ivanchowilliams)

Personal de la dirección de estadística y censos dependiente de la subsecretaría de sistemas de tecnología de la información de la provincia de Corrientes.

Gracias a la difusión de Nora Bär (La Nación), Jorge Aliaga (UBA-CONICET), Grandata, Jorge Montanari (CONICET), Andy Tow (datos electorales Página 12), Flor Coelho (La Nación Data).

Todos los recolectores de datos no oficiales que hacen un super esfuerzo diariamente recolectando y generando data para todos los proyectos.


## Sugerencias

Toda sugerencia es bienvenida!

Tenés nuevas fuentes de partes diarios provinciales? Escríbanme a [@vlasvlasvlas](https://twitter.com/vlasvlasvlas)
