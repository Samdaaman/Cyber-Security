import requests


def run():
    # https://webhook.site/#!/43700ede-bfcd-4e18-813c-b9bdeb973854/c3918803-e6c5-451a-a02e-953a9179f964/1
    url = 'https://webhook.site/43700ede-bfcd-4e18-813c-b9bdeb973854'
    params = {'user':'sam', 'pass':'123'}
    cookies = {'cookiejar':'yumyum'}
    headers = {'referer':'www.fake.com'}

    r_get = get(url, params, cookies, headers)
    print(r_get.content)

    r_post = post(url, params, cookies, headers)
    print(r_post.content)


def get(url, params, cookies, headers):
    response = requests.get(url, params, cookies=cookies, headers=headers)
    return response


def post(url, params, cookies, headers):
    response = requests.post(url, params, cookies=cookies, headers=headers)
    return response


if __name__ == '__main__':
    run()
