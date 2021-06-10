<?php
include("Mail.php");
header('charset:windows1251');

$HOSTNAME=$argv[1];
$SHORTDATETIME=$argv[2];
$HOSTSTATE=$argv[3];
$HOSTADDRESS=$argv[4];

$dbhost = '10.2.245.75';
$dbuser = 'nagiosAKT';
$dbpass = 'nagiosAKT';
$conn = mssql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect to DB ');
}

$sql = "SELECT * FROM dbo.nagiosAKT ";

mssql_select_db('OT_Monitoring');

$retval = mssql_query( $sql, $conn );
if(! $retval )
    {
    $data = "MSSQL error: " . mssql_get_last_message() . "  Error: "."  $SHORTDATETIME  $HOSTNAME  $HOSTSTATE  $HOSTADDRESS\n";
    $file = '/var/spool/nagios/mssql_automon.log';
    file_put_contents($file, $data, FILE_APPEND | LOCK_EX);
    die('Could not enter data: ');
    }

while($row = mysqli_fetch_assoc($retval)) {
        echo "$row";
    }

mssql_close($conn);

?>
