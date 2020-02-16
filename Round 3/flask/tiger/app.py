#!/usr/bin/env python3
from flask import Flask, redirect, render_template, abort, request
import auth
app = Flask(__name__)


@app.route('/')
def page_redirect_to_index():
    return redirect('/index')


@app.route('/index')
def page_index():
    return render_template('index.html')


@app.route('/names/')
def page_names_blank():
    return 'please specify name'


@app.route('/names/<name>')
def page_names(name):
    return render_template('names.html', name=name)


@app.route('/admin/')
def page_admin_redirect():
    return redirect('/admin/login')


@app.route('/admin/login', methods=['GET', 'POST'])
def page_login():
    error = ''
    code = None
    if request.method == 'POST':
        error, code = auth.try_login(request)
    if auth.is_authed():
        return redirect('/admin/dashboard')
    else:
        return render_template('login.html', error=error), code


@app.route('/admin/logout')
def page_logout():
    if auth.is_authed():
        auth.logout()
        return page_login()
    else:
        abort(403)


@app.route('/admin/<req_page>')
def page_admin(req_page):
    if not auth.is_authed():
        abort(403)

    if req_page == 'dashboard':
        return render_template('dashboard.html', username=auth._identity()[1])
    elif req_page == 'settings':
        return abort(501)
    elif req_page == 'database':
        return abort(501)
    elif req_page == 'run':
        return abort(501)
    else:
        return abort(404)


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
    app.secret_key = 'yeet'
    app.run(debug=True)
