#!/usr/bin/env python3
from flask import Flask, redirect, render_template
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
def page_admin_redirect:
    return redirect('/admin/login')

@app.route('/admin/<req_page>')
def page_admin(req_page):
    

@app.errorhandler(404)
def page_not_found(e):
    return "404 page not found", 404

@app.errorhandler(403)
def page_forbidden(e):
    return "403 Get outta here boi", 403

if __name__ == "__main__":
    app.run(debug=True)
