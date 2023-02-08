<?php

error_reporting(E_ALL);                             // this is for diplaying all errors
ini_set('Diplay errors',1);                         // this is for ini file file errors

$url="http://usindh.edu.pk";


if (isset($_GET["url"])){
    $url=$_GET["url"];
}

$file =fopen('io/url.txt','w') or die("unable to open file!");
fwrite($file,$url);
fclose($file);

echo $url;

//exec('python3 p100-B 2>&1', $output, $err);
exec('python3.6 Hrank_v2.py 2>&1', $output, $err);
if($err==1) {
    echo "PYTHON FAILED\n";
var_dump($output);
echo "<pre>   $err</pre>";
    die();
}








//$link ="http://www.intersport.co.uk/en/stores/bristol-dw-sports-s10271";



?>
