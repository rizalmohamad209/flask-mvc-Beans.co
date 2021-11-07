
from flask import Flask  # import Flask




app = Flask(__name__,template_folder='template')
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://yigsixorqpqayl:cad481ec2d71a0ceb5fc6ebb8ea20c44a65c0bbe4f5dd424e89e1357099b6646@ec2-54-145-49-132.compute-1.amazonaws.com:5432/d2qa5s6jf0t5jt'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from app.controllers import *


