from main_form import *
from req_class import *
from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import render_template, request
from secret_key import *

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key



@app.route("/")
def hello(name=None):
    form = main_form()
    return render_template('index.html', form=form)


@app.route("/handler", methods=["POST"])
def soup_it():
    form = main_form()
    if request.method == "POST":
        processed_dict = {}
        processed_dict["url"]  = form.url.data
        processed_dict["images"] = form.images.data
        processed_dict["links"] = links
        processed_dict["text"] = form.links.data
        return get_site(processed_dict)


def get_site(dictionary):
    req = req_class(dictionary)
    return req.parse_tags()


if __name__ == "__main__":
    app.run(host='0.0.0.0')