#!/usr/bin/php
<?php
$host=php_uname('n');
exec('netstat -tanpu|grep "5.196.212.145:22"|grep "ESTABLISHED"',$o);
if (count($o)==0) {
	exec('ssh autossh@mv226.prwh.com "netstat -tanpu|grep \"127.0.0.1:22\"| cut -f 2 -d \":\"|cut -f 1 -d \" \""',$o);
	for ($i=100;$i<999;$i++) {
		$trouve=false;
		foreach ($o as $ou){
			$v=intval(substr($ou,2));
			if ($v==$i) $trouve=true;
		}
		if ($trouve==false) break;
	}
	exec('autossh -f -q -N -M 0  -o "ServerAliveInterval 60" -o "ServerAliveCountMax 4800" -4 -p 22 -R 22'.$i.':localhost:22   autossh@mv226.prwh.com');
	$url='https://radioamateur.gp/antilles.php?c='.$host.'&s=3&v='.$i;
//echo $url;
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, $url);
	curl_setopt($curl, CURLOPT_COOKIESESSION, true);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
	$return = curl_exec($curl);
	curl_close($curl);
echo $return;
}
?>
