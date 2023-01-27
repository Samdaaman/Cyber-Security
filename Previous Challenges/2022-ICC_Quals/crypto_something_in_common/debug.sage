from sage.all import *
import random
import functools

def get_safe_prime():

    while True:

        z = random_prime(2^512 - 1, False, 2^511)

        if ZZ(z).is_prime():
            return z


def encrypt_message(M, p, q, e):
    """
    Using two secure primes, encrypt our message.
    Return the ciphertext with our public key
    """

    N = p*q

    C = pow(M, e, N)

    return C, e, N

def get_some_options(count, p, q):
    phi = (p-1)*(q-1)

    options = []

    while True:
        n = random.randint(51, 100001)

        if gcd(n, phi) == 1:
            if len(options) > 0:
                if not functools.reduce(lambda a,b: a and b, [gcd(n,x) for x in options]):
                    continue
            options.append(n)

        if len(options) == count:
            break
            
    return options

def print_options(options):
    print("Options:")
    for i,o in enumerate(options):
        print(f"\t{i}. {o}")

if __name__ == "__main__":

    with open("flag.txt", "rb") as f:
        flag = M = int.from_bytes(f.read().strip(), byteorder='big')

    # Generate secure primes
    q = get_safe_prime()
    p = get_safe_prime()

    print("Welcome to the totally awesome secure message encryptor!")
    print("I heard about this encryption standard and wanted to try implement it myself.")
    print("So I made a demonstration program. Give it a go! You can choose a few options")
    print("for encrypting, and it'll give you back the encrypted message and the public")
    print("key. ")

    options = get_some_options(5, p, q)
    
    while True:
        print_options(options)
        e_choice = int(input("> "))

        if e_choice not in range(len(options)):
            print("Please select again...")
            continue
        e = options[e_choice]

        print("Generating random number.......")
        C, e, N = encrypt_message(M, p, q, e)
        print("A sample encrypted text!")
        print("C:", C)  
        print("e:", e)
        print("N:", N)

        print("Would you like to generate a new one? [Y/n]")
        o = input("> ")
        if o != "Y":
            print("See you some other time!")
            break








