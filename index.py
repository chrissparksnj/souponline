from main_form import *
from req_class import *
from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import render_template, request, jsonify
from secret_key import *

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key



@app.route("/")
def hello(name=None):
    return render_template('index.html')


@app.route("/handler", methods=["POST"])
def soup_it():
    if request.method == "POST":
        return str(get_site(request.json))


def get_site(dictionary):
    req = req_class(dictionary)
    return req.parse_tags()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
