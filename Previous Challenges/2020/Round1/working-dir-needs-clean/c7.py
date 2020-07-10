import base64
from try_flag import names
for kp in names:
    ct = b'h2yv:94p6qrs7naeh'
    key = kp.encode('utf-8')*60

    bct = base64.decodebytes(ct)
    bkey = base64.decodebytes(key)

    pt = bytes([a^b for a,b in zip(bct, bkey)])
    print(base64.encodebytes(pt))

