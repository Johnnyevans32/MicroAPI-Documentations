
from flask import Flask, render_template, url_for, redirect, flash
import requests
import json
import hashlib

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def docs_titles():
    flash(u'These are all the Microapi Available for documentation viewing', 'message')
    return render_template("index.html", value=data)


@app.route('/docs/<_id>')
def data(_id):

    def check_microapi(microapi, data):
        if microapi:
            if microapi in data['microapi']:
                documentation = data['microapi'][microapi]
                return documentation
            else:
                return "Microapi is not in Database"
        else:
            return "Invalid Entry"

    return render_template("docs.html", value=check_microapi(_id, data))

def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

with open("docs.json","r") as read_file:
    data = json.load(read_file, object_hook=as_complex)
