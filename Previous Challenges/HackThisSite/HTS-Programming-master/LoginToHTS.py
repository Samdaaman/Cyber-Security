import requests

s = requests.session()
cookie = {}


def login_and_get(levelurl):
    global cookie
    cookie = {'PHPSESSID': input("Enter PHPSESSID: ")}
    response = s.get(levelurl, cookies=cookie)
    content_string = response.content.decode("utf-8")
    return content_string


def login_and_get_with_phpsessid(levelurl, phpsessid):
    global cookie
    cookie = {'PHPSESSID': phpsessid}
    response = s.get(levelurl, cookies=cookie)
    content_string = response.content.decode("utf-8")
    return content_string


def post_data(url, data):
    global cookie
    return s.post(url, data=data, cookies=cookie)


def post_data_with_headers(url, data, headerss):
    global cookie
    return s.post(url, data=data, cookies=cookie, headers=headerss)


def close_connection():
    s.close()


def run():
    # test the get
    print(login_and_get("https://www.hackthissite.org/missions/prog/11/"))


if __name__ == "__main__":
    run()
