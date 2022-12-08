

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_101177610013690114367644862496650410682060315507552683976670417670408764432851 = Integer(101177610013690114367644862496650410682060315507552683976670417670408764432851); _sage_const_14374457579818477622328740718059855487576640954098578940171165283141210916477 = Integer(14374457579818477622328740718059855487576640954098578940171165283141210916477); _sage_const_97329024367170116249091206808639646539802948165666798870051500045258465236698 = Integer(97329024367170116249091206808639646539802948165666798870051500045258465236698); _sage_const_0 = Integer(0); _sage_const_208913474430283759938044884583915265967 = Integer(208913474430283759938044884583915265967); _sage_const_3045783791 = Integer(3045783791); _sage_const_177776968102066079765540960971192211603 = Integer(177776968102066079765540960971192211603); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_32293793010624418281951109498609822259728115103695057808533313831446479788050 = Integer(32293793010624418281951109498609822259728115103695057808533313831446479788050); _sage_const_38685626227668133590597631 = Integer(38685626227668133590597631); _sage_const_59 = Integer(59); _sage_const_14771 = Integer(14771); _sage_const_27733 = Integer(27733); _sage_const_620059697 = Integer(620059697); _sage_const_2915987653003935133321 = Integer(2915987653003935133321); _sage_const_257255080924232005234239344602998871 = Integer(257255080924232005234239344602998871); _sage_const_100000000000000 = Integer(100000000000000); _sage_const_1 = Integer(1); _sage_const_16 = Integer(16)
from hashlib import sha1
from sage.all import *
from icecream import ic
from Crypto.Cipher import AES


p = _sage_const_101177610013690114367644862496650410682060315507552683976670417670408764432851 
Gx = _sage_const_14374457579818477622328740718059855487576640954098578940171165283141210916477 
Gy = _sage_const_97329024367170116249091206808639646539802948165666798870051500045258465236698 
a1 = _sage_const_0 
a2 = _sage_const_208913474430283759938044884583915265967 
a3 = _sage_const_3045783791 
a4 = _sage_const_177776968102066079765540960971192211603 
a6 = (pow(Gy, _sage_const_2 , p) + a3*Gy - (pow(Gx, _sage_const_3 , p) + a2*pow(Gx, _sage_const_2 , p) + a4*Gx)) % p

F = GF(p)
ec = EllipticCurve(F, [a1, a2, a3, a4, a6])

G = ec(Gx, Gy)

Gnx = _sage_const_32293793010624418281951109498609822259728115103695057808533313831446479788050 
Gn = ec.lift_x(Gnx)
ic(Gn)
n_limit = _sage_const_38685626227668133590597631 

ec_order = ec.order()
ic(ec_order)
order_factors = [p**k for p, k in factor(ec_order)]
order_factors = [_sage_const_3 **_sage_const_2 , _sage_const_59 , _sage_const_14771 , _sage_const_27733 , _sage_const_620059697 , _sage_const_2915987653003935133321 , _sage_const_257255080924232005234239344602998871 ]
num_small_factors = sum([i < _sage_const_100000000000000  for i in order_factors])
ic(num_small_factors)

residuals = []
for order_factor in order_factors[:num_small_factors]:
    ic(order_factor)
    t = int(ec_order // order_factor)
    dlog = discrete_log(t*Gn, t*G, operation='+')
    residuals.append(dlog)

ic(residuals)
n_base = crt(residuals, order_factors[:num_small_factors])

n_guess_step = _sage_const_1 
for order_factor in order_factors[:num_small_factors]:
    n_guess_step *= order_factor
ic((n_limit - n_base) // n_guess_step)

n = _sage_const_0 
for n_guess in range(n_base, n_limit, n_guess_step):
    Gn_test = n_guess * G
    if Gn_test == Gn:
        ic(Gn_test, Gn_test == Gn)
        n = n_guess
        break


ct = bytes.fromhex('df572f57ac514eeee9075bc0ff4d946a80cb16a6e8cd3e1bb686fabe543698dd8f62184060aecff758b29d92ed0e5a315579b47f6963260d5d52b7ba00ac47fd')
iv = bytes.fromhex('baf9137b5bb8fa896ca84ce1a98b34e5')

key = sha1(str(n).encode('ascii')).digest()[_sage_const_0 :_sage_const_16 ]
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
print(pt.decode())
