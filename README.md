# Covid19arData
COVID-19 Argentina data

El objetivo de este repo es poder compartir en formato CSV o tabular y abierto la información oficial proveniente de los partes diarios sobre la situación de COVID-19 en Argentina.

La informacion se completa en un google drive y se exporta en formato CSV en este repo.

También se esta tweetboteando en @Covid19arData. 

### Accesos
* Tweetbot: https://twitter.com/Covid19arData 
* Google Drive Data: https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/edit?usp=sharing


### Fuentes
* Parte diario Nacional: https://www.argentina.gob.ar/coronavirus/informe-diario
* Parte diario Santa Fe: https://www.santafe.gob.ar/index.php/web/content/view/full/234420/
* Parte diario BsAs: https://www.gba.gob.ar/saludprovincia/boletin_epidemiologico
* Parte diario GCBA: https://www.buenosaires.gob.ar/salud/noticias/actualizacion-de-los-casos-coronavirus-en-la-ciudad-buenos-aires
* Parte diario Rio Negro: https://salud.rionegro.gov.ar/sala/ 
* Partes diarios videos oficiales Casa Rosada: https://www.youtube.com/user/casarosada/videos


### Descripción de columnas de la tabla
* fecha : fecha a la que corresponde los datos.
* dia_inicio : cant dias desde el inicio del caso 1.
* dia_cuarentena_dnu260: cant dias desde la cuarentena por DNU 260.
* osm_admin_level_2: nombre administrativo en OpenStreetMap escala país.
* osm_admin_level_4: nombre administrativo en OpenStreetMap escala provincia.
* osm_admin_level_8: nombre administrativo en OpenStreetMap escala ciudad.
* tot_casosconf: total de casos de infectados confirmados.
* nue_casosconf_diff: nuevos casos infectados del dia.
* casosconf_DGRate: Daily growth rate, Ratio de incremento de casos diarios (DGR,RIC). Esto es TotalCasosDiaActual / TotalCasosDiaAnterior
* tot_fallecidos: total de fallecidos.
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