<?php

// https://smapache.com.ar/proyectos/covid19ar/get_historico.php
// https://github.com/SistemasMapache/Covid19arData
// Covid19arData
// Total datos historicos

$data = file_get_contents('https://spreadsheets.google.com/feeds/list/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/1/public/full?alt=json');
$json_data= json_decode($data,true);

echo json_encode($json_data['feed']['entry']);