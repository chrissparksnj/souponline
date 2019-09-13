from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, BooleanField


class main_form(FlaskForm):
    url = StringField("url")
    images = BooleanField("images")
    links = BooleanField("links")
    text = BooleanField("text")