import requests
import time
import datetime


def make_guess(guess, guesses):
    try:
        #print(f'trying guess {guess}')
        res = requests.get('http://192.168.1.1', auth=('admin', guess))
        if res.status_code == 200:
            print(f'\n------------------\nFound password {guess}\n--------------------')
            exit(0)

    except KeyboardInterrupt:
        print(f'At guess {guess} which is number {guesses.index(guess)} : {guesses.index(guess) / len(guesses) * 100} - type a to abort')
        make_guess(guess, guesses)

    except Exception as e:
        print(f'Other error with guess: {guess} -- {e}')
        time.sleep(1)
        make_guess(guess, guesses)


def main():
    guesses = generate_guesses()
    print(f'Started at: {datetime.datetime.now().time()}')
    for guess in guesses:
        make_guess(guess, guesses)


def main2():
    guesses = generate_guesses()
    guesses_trim = guesses[guesses.index('132000') : len(guesses)]
    with open('guesses.txt', 'w') as fh:
        fh.writelines([i + '\n' for i in guesses_trim])


def generate_guesses():
    alphabet = '0123456789abcdef'

    guesses = []
    i = 1
    for i in range(len(alphabet)):
        c1 = alphabet[i]
        print(f'Generating --- {(i+1) / len(alphabet) * 100}% of the way there!')
        for c2 in alphabet:
            for c3 in alphabet:
                for c4 in alphabet:
                    for c5 in alphabet:
                        for c6 in alphabet:
                            guesses.append(c1+c2+c3+c4+c5+c6)


    print(f'Generating --- {len(guesses)} guesses generated\n')
    return guesses


if __name__ == '__main__':
    main2()
