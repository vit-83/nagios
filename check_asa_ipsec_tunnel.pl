#!/usr/bin/perl -w

unless (($#ARGV == 2) or ($#ARGV == 3)) { print("usage:\tcheck_asa_l2lvpn <IP address> <community> <peer IP> [friendlyname]\n"); exit(1);}

$IP = $ARGV[0];
$community = $ARGV[1];
$peerip = $ARGV[2];
if (defined($ARGV[3])) { $friendlyname = $ARGV[3]; }

$uptunnels = `/usr/local/bin/snmpwalk -v1 -c $community $IP 1.3.6.1.4.1.9.9.171.1.2.3.1.7`;

$state = "CRIT";
$msg = "IPsec tunnel to peer ".$peerip." is down!";
$output = "value=1";

foreach (split("\n", $uptunnels)) {
	if ($_ =~ /SNMPv2-SMI::enterprises.9.9.171.1.2.3.1.7.\d+ = STRING: "$peerip"/) {
		$state = "OK";
		$msg = "IPsec tunnel to peer ".$peerip." is up.";
	}
}

print "VPN-".$friendlyname." " . $state . " " . $msg . " | " . $output . "\n";

if ($state eq "OK") { exit 0;
} elsif ($state eq "WARN") { exit 1;
} elsif ($state eq "CRIT") { exit 2;
} else { #unknown!
	exit 3;
}

