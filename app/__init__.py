
from flask import Flask  # import Flask




app = Flask(__name__,template_folder='template')
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://vqweqxctlhtdui:343a3b2e105a6561d318288e85a8e4b167e45569008828e0e9810f95efb82ba7@ec2-54-145-49-132.compute-1.amazonaws.com:5432/d1cug2tsr3c6v4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from app.controllers import *


