# Covid19arData
COVID-19 Argentina data

El objetivo de este repo es poder compartir en formato CSV o tabular y abierto la información oficial proveniente de los partes diarios sobre la situación de COVID-19 en Argentina.

La informacion se completa en un google drive y se exporta en formato CSV en este repo.

También se esta tweetboteando en @Covid19arData. 

### Accesos
* **Google Drive Data: https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/edit?usp=sharing**

* Data histórica en CSV: https://raw.githubusercontent.com/SistemasMapache/Covid19arData/master/CSV/Covid19arData%20-%20historico.csv
* Data histórica en XLS: https://github.com/SistemasMapache/Covid19arData/raw/master/XLS/Covid19arData%20-%20historico.xlsx

* Tweetbot: https://twitter.com/Covid19arData 

### Fuentes
* Parte diario Nacional: https://www.argentina.gob.ar/coronavirus/informe-diario
* Parte diario Santa Fe: https://www.santafe.gob.ar/index.php/web/content/view/full/234420/
* Parte diario BsAs: https://www.gba.gob.ar/saludprovincia/boletin_epidemiologico
* Parte diario GCBA: https://www.buenosaires.gob.ar/salud/noticias/actualizacion-de-los-casos-coronavirus-en-la-ciudad-buenos-aires
* Parte diario Rio Negro: https://salud.rionegro.gov.ar/sala/, https://www.rionegro.gov.ar/?buscar&temas=144&catView=3
* Parte diario Misiones: https://coronavirus.misionesonline.net/
* Parte diario San Luis: http://www.sanluis.gov.ar/coronavirus/
* Parte diario Corrientes: https://www.corrientes.gob.ar/home/salud/categorias
* Parte diario Neuquen: https://www.saludneuquen.gob.ar/
* Parte diario Chaco: http://comunicacion.chaco.gov.ar/lista-noticias/328
* Parte diario Tierra del fuego: https://www.facebook.com/saludtdf
* Parte diario Mendoza: http://www.salud.mendoza.gov.ar/, http://www.prensa.mendoza.gov.ar/salud/
* Parte diario Cordoba (difusion): https://www.lavoz.com.ar/temas/coronavirus-en-cordoba, https://cdn.lavoz.com.ar/sites/default/files/file_attachments/nota_periodistica/PARA_PRENSA_-_29.03.2020_Informe_EPIDEMIOLOGICO_casos_confirmados.pdf
* Partes diarios videos oficiales Casa Rosada: https://www.youtube.com/user/casarosada/videos
* Chequeo extra: Wiki Pandemia de enfermedad por coronavirus 2020 Argentina: https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina
* Tabla de datos diarios de Jorge Aliaga @jorgeluisaliaga: https://docs.google.com/spreadsheets/d/1M7uDgWSfy6z1MNbC9FP6jTNgvY7XchJ0m-BfW88SKtQ/edit#gid=0


### Descripción de columnas de la tabla
* fecha : fecha a la que corresponde los datos.
* dia_inicio : cant dias desde el inicio del caso 1.
* dia_cuarentena_dnu260: cant dias desde la cuarentena por DNU 260.
* osm_admin_level_2: nombre administrativo en OpenStreetMap escala país.
* osm_admin_level_4: nombre administrativo en OpenStreetMap escala provincia.
* osm_admin_level_8: nombre administrativo en OpenStreetMap escala ciudad.
* tot_casosconf: total de casos de infectados confirmados. Columna que sumariza fila a fila el total de casos confirmados.
* nue_casosconf_diff: nuevos casos infectados del dia.
* tot_fallecidos: total de fallecidos. Columna que sumariza fila a fila el total de fallecidos.
* nue_fallecidos_diff: nuevos casos fallecidos del dia.
* transmision_tipo: tipo de transmision al dia de la fecha.
* informe_link: url de acceso al informe de donde sale el dato.
* observacion: observaciones relacionadas al dato. Se sumó porque encontramos diferencias entre cantidades informadas en partes diarios provinciales vs partes diarios nacionales.


### Ayudan en esto

Vladimiro Bellini @vlasvlasvlas

Damián Castiñeiras @damcast

Leandro Stryjek

Andres Snitcofsky @rusosnith

Telegram channel Usuaries de datos Argentina @daterxsargentina

Nadia Perez Laureda

Toda sugerencia es bienvenida! Tenés nuevas fuentes de partes diarios provinciales? Escriban por Issues o manden tw a @vlasvlasvlas, @damcast