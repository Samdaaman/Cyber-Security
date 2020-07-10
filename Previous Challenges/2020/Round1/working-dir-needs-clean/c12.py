import requests


def make_req(ua):
    h = {"User-Agent": ua}
    r = requests.post('https://r1.nzcsc.org.nz/challenge12/secretagent', headers=h)
    return(r.text)


def main1():
    resps = []
    with open('ua.txt') as fh:
        data = fh.readlines()
    for ua_l in data:
        make_req('')


def main():
    while 1:
        print(make_req('s3cr3tAg3ntinput{{' + input('enter : ') + '}}'))

if __name__ == '__main__':
    main()
