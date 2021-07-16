import requests
names = ['Khnumhotep', 'Khnumhotep 2', 'Khnumhotep II', 'Khnumhotep ii', 'Beni Hasan', 'Beni Hasan 3', 'BH3', 'Niankhkhnum', 'khnumhotep', 'khnumhotep 2', 'khnumhotep ii', 'beni hasan', 'beni hasan 3', 'bh3', 'niankhkhnum', 'Khnumhotep2', 'KhnumhotepII', 'Khnumhotepii', 'BeniHasan', 'BeniHasan3', 'khnumhotep2', 'khnumhotepii', 'benihasan', 'benihasan3']


def tf(flag: str):
    r = requests.post('https://scoreboard.nzcsc.org.nz/actions/challenges', data={
            'flag': flag,
            'challenge': '15',
            'action': 'submit_flag',
            'xsrf_token': '2owkngdfcYK4sxixuDbWqW7XiTQWCXJSq8hHjEbMv/oI/y3ZjjVToGFt+k2ivDN6'
        },
        cookies={
            'PHPSESSID': '38b1ba98a140514d93356d3f80f57aa9',
            'login_tokens': '%7B%22t%22%3A%22ajQSKh6Y1O%2BWtC0x0ATCZL5jWgYONfQI6R0mWIrO5AP%5C%2FR%2BMFS0cMeyNyVZWOUbWm%22%2C%22ts%22%3A%22xwj8ifrusrtCr4WC%22%7D'
        },
        headers={
            'Referer': 'https://scoreboard.nzcsc.org.nz/challenges',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects=False
    )

    if r.headers.get('location') == 'https://scoreboard.nzcsc.org.nz/challenges?category=1&status=incorrect' and r.status_code == 302:
        print(f'Flag failed - {flag}')
        return False
    else:
        print(f'Weird response - Flag={flag} - {r.status_code}')
        print(r.text)
        print(r.headers.get('location', 'no location'))
        raise Exception(r)