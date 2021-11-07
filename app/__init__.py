
from flask import Flask  # import Flask

ENV ='dev'


app = Flask(__name__,template_folder='template')
if ENV == 'dev':
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:Rizalmohamad123@localhost/coffeshop'
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] =''
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost/berita'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from app.controllers import *


