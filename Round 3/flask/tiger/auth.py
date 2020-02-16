from flask import session


# TODO create user class
#


def is_authed():
    return _identity() is not None


def try_login(received_request):
    username = received_request.form.get('username')
    password = received_request.form.get('password')
    authed_user = _authenticate(username, password)
    if authed_user is not None:
        session[SESSION_KEY_USER_ID] = authed_user[0]
        print('authed with user:' + ','.join([str(i) for i in authed_user]))
        return '', 200
    else:
        return 'Incorrect username or password', 401


def logout():
    session.pop(SESSION_KEY_USER_ID, None)


def _identity():
    user_id = session.get(SESSION_KEY_USER_ID)
    if user_id is not None:
        for row in db:
            if row[0] == user_id:
                return row


def _init_db():
    global db
    db = [(1, 'sam', 'pass'), (2, 'bob', 'yeet')]
    print('db inited')


def _authenticate(username, password):
    if username is None or password is None:
        return None
    for row in db:
        if username == row[1] and password == row[2]:
            return row


SESSION_KEY_USER_ID = 'user_id'

db = []
_init_db()
