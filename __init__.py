from flask import Flask
from flask.ext.sqlalchemy import SQLALCHEMY


app = Flask(__name__)
app.config.from_object('settings')
db = SQLALCHEMY(app)

from blog import views
