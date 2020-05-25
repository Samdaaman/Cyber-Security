#!/usr/bin/env python3
from flask import Flask, redirect, render_template, abort, request, url_for, make_response
import auth
app = Flask(__name__)


@app.route('/')
def page_redirect_to_index():
    resp = redirect('/index')
    return resp


@app.route('/index')
def page_index():
    resp = make_response(render_template('index.html'))
    return resp


@app.route('/names/')
def page_names_blank():
    resp = make_response('please specify name')
    return resp


@app.route('/names/<name>')
def page_names(name):
    resp = render_template('names.html', name=name)
    return resp


@app.route('/admin/')
def page_admin_redirect():
    resp = redirect(url_for('page_login'))
    return resp


@app.route('/admin/login', methods=['GET', 'POST'])
def page_login():
    error = ''
    code = None
    token = None
    if request.method == 'POST':
        error, code, token = auth.try_login(request)
    if token is not None:
        resp = redirect(url_for('page_admin', req_page='dashboard'))
        auth.set_token_cookie(token, resp)
        return resp
    else:
        resp = make_response(render_template('login.html', error=error), code)
        return resp


@app.route('/admin/logout')
def page_logout():
    if auth.is_authed():
        resp = redirect(url_for('page_login'))
        resp.delete_cookie('token')
        return resp
    else:
        abort(403)


@app.route('/admin/<req_page>')
def page_admin(req_page):
    if not auth.is_authed():
        abort(403)

    if req_page == 'dashboard':
        resp = make_response(render_template('dashboard.html', username=auth.current_user().username))
    elif req_page == 'settings':
        abort(501)
    elif req_page == 'database':
        abort(501)
    elif req_page == 'run':
        abort(501)
    else:
        abort(404)

    auth.refresh_token(resp)
    return resp


@app.errorhandler(404)
def page_not_found(e):
    return '404 page not found', 404


@app.errorhandler(403)
def page_forbidden(e):
    return '403 Get outta here boi<br>use <a href="/admin/login">This</a> page to login', 403


@app.errorhandler(501)
def page_not_implemented(e):
    return "501 Sorry dev\'s haven\'t given this one a yarn yet", 501


if __name__ == '__main__':
    app.secret_key = auth.secret_key
    app.run(debug=False, host='0.0.0.0')
