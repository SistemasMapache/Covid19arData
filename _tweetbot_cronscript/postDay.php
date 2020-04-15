<?php
/*
TODO 26/3/2020
- chequeo de tw length.
- audit log success fail.
*/

// emoji table 
// https://apps.timwhitlock.info/emoji/tables/unicode

// https://github.com/abraham/twitteroauth
require_once "twitteroauth-master/autoload.php";
use Abraham\TwitterOAuth\TwitterOAuth;

// defines
define('CONSUMER_KEY', ''); //add key
define('CONSUMER_SECRET', ''); //add key
define('ACCESS_TOKEN', ''); //add key
define('ACCESS_TOKEN_SECRET', ''); //add key

//date
date_default_timezone_set('America/Argentina/Buenos_Aires');
$now = date('j/m/Y', strtotime( '-1 days' ));

//vars
$confirmados = '';
$fallecidos = '';

// https://github.com/SistemasMapache/Covid19arData
$data = file_get_contents('https://spreadsheets.google.com/feeds/list/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/1/public/full?alt=json');
$json_data= json_decode($data,true);
$arr= $json_data['feed']['entry'];

$results = array_filter($arr, function($data) {
    global $now;
    if( $data['gsx$fecha']['$t'] == $now )
        return true; 
});
$arrayDay = array_merge($results);

// confirmados
$confirmados .= "\u{1F6A8}\u{1F4CB} COVID-19 Argentina. Confirmados $now.\n\n";
foreach ($arrayDay as &$val) {

    $confirmados .= $val['gsx$osmadminlevel4']['$t'];
    if ($val['gsx$osmadminlevel8']['$t'] !== '' ) {
        $confirmados .= ", ".$val['gsx$osmadminlevel8']['$t'];
    }
    $confirmados .= ": ".$val['gsx$nuecasosconfdiff']['$t'];
    $confirmados .= ".\n";
}
$confirmados .= "\nTotal de confirmados: ".$val['gsx$totcasosconf']['$t']."\n";
$confirmados .= "\u{1F517} Más info : https://tinyurl.com/covid19ar";

// fallecidos
$fallecidos .= "\u{1F6A8}\u{1F4CB} COVID-19 Argentina. Fallecidos $now.\n\n";
$fallbool = false;
foreach ($arrayDay as &$val) {

    if ($val['gsx$nuefallecidosdiff']['$t'] !== '0' ) {
        $fallbool = true;
        $fallecidos .= $val['gsx$osmadminlevel4']['$t'];
        if ($val['gsx$osmadminlevel8']['$t'] !== '' ) {
            $fallecidos .= ", ".$val['gsx$osmadminlevel8']['$t'];
        }
        $fallecidos .= ": ".$val['gsx$nuefallecidosdiff']['$t'];
        $fallecidos .= ".\n";
    }

}
if ($fallbool == false ) {
    $fallecidos .= "Sin fallecidos en el día de la fecha.\n";
}
$fallecidos .= "\nTotal de fallecidos: ".$val['gsx$totfallecidos']['$t']."\n";
$fallecidos .= "\u{1F517} Más info : https://tinyurl.com/covid19ar";



//conn
$connTW = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);

//post confirmados
$statueConf = $connTW->post('statuses/update', array('status' =>$confirmados));
if ($connTW->getLastHttpCode() == 200) {
    // Tweet posted succesfully
} else {
    // Handle error case
}

//post fallecidos
$statueFall = $connTW->post('statuses/update', array('status' =>$fallecidos));
if ($connTW->getLastHttpCode() == 200) {
    // Tweet posted succesfully
} else {
    // Handle error case
}

?>