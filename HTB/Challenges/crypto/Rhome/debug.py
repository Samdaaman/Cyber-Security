from Crypto.Util.number import isPrime, long_to_bytes, getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randint
from hashlib import sha256
from icecream import ic

# from secret import FLAG
FLAG = b'HTB{FAKE_FLAG}'


class DH:

    def __init__(self):
        self.gen_params()

    def gen_params(self):
        # self.r = getPrime(512)

        # while True:
        #     self.q = getPrime(42)
        #     self.p = (2 * self.q * self.r) + 1
        #     if isPrime(self.p):
        #         break

        # while True:
        #     self.h = getPrime(42)
        #     self.g = pow(self.h, 2 * self.r, self.p)
        #     if self.g != 1:
        #         break

        # self.a = randint(2, self.p - 2)
        # self.b = randint(2, self.p - 2)

        # self.A, self.B = pow(self.g, self.a, self.p), pow(self.g, self.b, self.p)
        # self.ss = pow(self.A, self.b, self.p)

        # ic(self.r)
        # ic(self.q)
        # ic(self.p)
        # ic(self.h)
        # ic(self.g)
        # ic(self.a)
        # ic(self.b)
        # ic(self.A)
        # ic(self.B)
        # ic(self.ss)

        self.r = 10551042130823381679006949160921494851701939464552887939496269011875357591310539899826194792382525995606845381036041920132809526962045548193196938847293809
        self.q = 3965194668311
        self.p = 83673872004531211172026628100008293083209131977966378870336121281930272528702224307779319252661011349165240627636541302074614450661618017907995402558591451315437573199
        self.h = 3941112718709
        self.g = 38251193272942620516880149429584442354178557610248802173739406939990082141276490984517630274106204777699055836989495581884101326447272981141986799190227639290316818512
        self.a = 53837517070618811206568249123737584100464232706836189040023680440184277603267546219453847766047604697201442353230278852991398211773843050339974922449827377358081185338
        self.b = 29785509673532072755627897894315458583748117699378975278380820686457048216129240326175259248726611301692775824307895210995509301524498173047239897067951056872633653481
        self.A = 58893684601083641472008343824811384479289268943843247548884976840862379353658139504172263455161167867304119253188678138838820498376619665062256855371666377507239697002
        self.B = 75139637223778419361338996624025281308132049508208900826980478416520252028271490500323030314331619486693147038752197759528062211332614115658040339163768066741087843889
        self.ss = 20322516136066642713166055381650860852288135158290407352446807262420456488707076058142436004080511247290713866138178747815040365622033260639801312398964977644197826117

    def encrypt(self, flag_part):
        key = sha256(long_to_bytes(self.ss)).digest()[:16]
        cipher = AES.new(key, AES.MODE_ECB)
        ct = cipher.encrypt(pad(flag_part, 16)).hex()
        return f"encrypted = {ct}"

    def get_params(self):
        return f"p = {self.p}\ng = {self.g}\nA = {self.A}\nB = {self.B}"


def menu():
    print("\nChoose as you please\n")
    print("1. Get parameters")
    print("2. Reset parameters!! This can take some time")
    print("3. Get Flag")

    option = input("\n> ")
    return option


def main():
    dh = DH()

    while True:
        choice = int(menu())
        if choice == 1:
            print(dh.get_params())
        elif choice == 2:
            dh.gen_params()
        elif choice == 3:
            print(dh.encrypt(FLAG))
        else:
            print('See you later.')
            exit(1)


if __name__ == "__main__":
    main()
