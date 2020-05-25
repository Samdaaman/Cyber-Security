import auth
import time
import datetime
import base64

secret = 'yeet'
token1 = auth.gen_auth_token([["1"]], secret, datetime.timedelta(seconds=1))
print(token1.decode('utf-8'))
print('Test1(t)', auth.check_auth_token(token1, [[["1"]]], secret))
print('Test2(f-in)', auth.check_auth_token(token1, [[["1"]]], 'yeeet'))
print('Test3(f-no user)', auth.check_auth_token(token1, [0], secret))
time.sleep(2)
print('Test4(f-ex)', auth.check_auth_token(token1, [[["1"]]], secret))

token2 = auth.gen_auth_token('admin', 'not a secret', datetime.timedelta(days=1))
print(token2.decode('utf-8'))
print('Test5(f)', auth.check_auth_token(token2, ['admin'], secret))

header, payload = token2.decode('utf-8').split('.')[0:2]
header_str = base64.b64decode(header).decode('utf-8')
header_str_mod = header_str.replace('HS256', 'none')
header_mod_nt = base64.b64encode(header_str_mod.encode('utf-8')).decode('utf-8')
header_mod = header_mod_nt.replace('=', '')
token3 = header_mod + '.' + payload
print('Test6(f-unk)', auth.check_auth_token(token3, ['admin'], secret))
