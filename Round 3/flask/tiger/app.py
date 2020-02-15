#!/usr/bin/env python3
from flask import Flask, redirect, render_template
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

if __name__ == "__main__":
    app.run(debug=True)
