from hashlib import sha256
from pwn import *
import netsquid as ns
from random import seed
from util import measure, bitsToHex, bitsToHash, randomBasis
from icecream import ic


# From part 1
private_key = 3262827136301000405966

seed(private_key)
q_server_key = []
q_user_key = []

def randomBasisLetter():
    r = randint(0, 1)
    return "Z" if r else "X"

random_basises = [randomBasis() for _ in range(256)]
opposite_basises = [(ns.Z if i == ns.X else ns.X) for i in random_basises]


for i in range(256):
    qubits = ns.qubits.create_qubits(2)
    q1, q2 = qubits[0], qubits[1]
    ns.qubits.operate(q1, ns.X)
    ns.qubits.operate(q1, ns.H)
    ns.qubits.operate(q2, ns.X)
    ns.qubits.combine_qubits([q1, q2])
    ns.qubits.operate([q1, q2], ns.CX)
    q_server_key.append(measure(q1, random_basises[i]))
    q_user_key.append(measure(q2, random_basises[i])) # we can control this


print(q_server_key)
print(q_user_key)

q_server_key = bitsToHash(q_server_key)
q_user_key = bitsToHex(q_user_key)

# if q_server_key and q_user_key are measured using the same basis they are opposite value
user_key_bitflipped = bytes([i ^ 255 for i in bytes.fromhex(q_user_key)])
server_key_test = sha256(user_key_bitflipped).digest()
ic(q_server_key.hex())
ic(server_key_test.hex())