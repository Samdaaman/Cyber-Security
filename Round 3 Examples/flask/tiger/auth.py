from flask import request
import jwt
import datetime

# jwt stuff
def _gen_auth_token(subject, secret, expiry_time):
    payload = {
        'exp': datetime.datetime.utcnow() + expiry_time,
        'iat': datetime.datetime.utcnow(),
        'sub': subject
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token


def _get_sub_from_token(token, secret):
    try:
        payload = jwt.decode(token, secret)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        print('JWT Signature Expired')
    except jwt.InvalidTokenError:
        print('JWT Invalid Token')
    except Exception as e:
        print('JWT Unknown Error:', e)


# Abstraction functions
def _get_token_for_user(user):
    return _gen_auth_token(user.username, secret_key, datetime.timedelta(seconds=5))


def _get_user_from_token(token):
    sub = _get_sub_from_token(token, secret_key)
    return _get_user(username=sub, require_password=False)


def set_token_cookie(token, response):
    if token is not None:
        response.set_cookie('token', token)


def refresh_token(response):
    if current_user() is not None:
        token = _get_token_for_user(current_user())
        set_token_cookie(token, response)
        print('Refreshed token for:', current_user().username)
# End JWT Stuff


# TODO refresh JWT tokens
#


class User(object):
    def __init__(self, db_row):
        self.username = db_row[0]
        self.password = db_row[1]

    def to_db_row(self):
        return [self.username, self.password]


def is_authed():
    return current_user() is not None


def try_login(received_request):
    username = received_request.form.get('username')
    password = received_request.form.get('password')
    authed_user = _get_user(username=username, password=password)
    if authed_user is not None:
        token = _get_token_for_user(authed_user)
        print('Authed with user:' + ','.join([str(i) for i in authed_user.to_db_row()]))
        print('Token:', token)
        return '', 200, token
    else:
        return 'Incorrect username or password', 401, None


def current_user():
    return _get_user_from_token(request.cookies.get('token'))


def _init_db():
    global db
    db = [('sam', 'pass'), ('bob', 'yeet')]
    print('db inited')


def _get_user(username=None, password=None, require_password=True):
    for row in db:
        user = User(row)
        if username is not None:
            if user.username == username:
                if require_password is False or user.password == password:
                    return user


secret_key = 'yeet'
db = []
_init_db()
