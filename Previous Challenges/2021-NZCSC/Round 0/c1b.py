import requests as r

url = 'https://www.devglan.com/online-tools/jasypt-online-encryption-decryption/decrypt'

with open('c1b_output.txt', 'wb', buffering=0) as out:
    with open('rockyou.txt', 'r') as fh:
        while True:
            password = fh.readline().strip()

            print(f'Trying "{password}"')
            data = {
                'inputString': "V+QQEMfkRgUXVy8d8aI93UfMI9auuIGkco2Zm7Gs2bc+pFS1hgR7+ppKqHgyn3XeLGpUggbuAMU=",
                'secretKey': password
            }
            res = r.post(url, json=data)

            if res.json()['outputString'] == 'Invalid encryption key.':
                pass
            else:
                line = f"Found: {password}: {[res.json()['outputString']]}"
                out.write(f'{line}\n'.encode())
                print(line)
