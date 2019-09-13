from main_form import *
from req_class import *
from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key_123"
@app.route("/")
def hello(name=None):
    form = main_form()
    return render_template('index.html', form=form)

@app.route("/handler", methods=["POST"])
def soup_it():
    form = main_form()
    if request.method == "POST":
        processed_dict = {}
        url = form.url.data
        images = form.images.data
        links = form.links.data
        text =  form.text.data

        processed_dict["url"] = url
        processed_dict["images"] = images
        processed_dict["links"] = links
        processed_dict["text"] = text
        return get_site(processed_dict)



def get_site(dictionary):
    req = req_class(dictionary)
    return req.parse_tags()


if __name__ == "__main__":
    app.run(host='0.0.0.0')