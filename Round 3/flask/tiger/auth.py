from flask import Flask
from flask_jwt import jwt_required, current_identity, JWTError, JWT


def init(app):
    JWT(app, _authenticate, _identity)


@jwt_required()
def _test_jwt():
    return


def is_authed():
    try:
        _test_jwt()
        return True
    except JWTError:
        return False


def try_auth(received_request):
    username = received_request.form.get('username')
    password = received_request.form.get('password')
    if username is None or password is None:
        return '401 - Incorrect auth present', 401
    if _authenticate(username, password) is not None:
        return '', 200
    else:
        return 'Incorrect username or password', 401


def _init_db():
    global db
    db = [(1, 'sam', 'pass'), (2, 'bob', 'yeet')]
    print('db inited')


def _authenticate(username, password):
    for row in db:
        if username == row[1] and password == row[2]:
            return row


def _identity(payload):
    user_id = payload['identity']
    for row in db:
        if row[0] == user_id:
            return row
    return None


db = []
_init_db()
