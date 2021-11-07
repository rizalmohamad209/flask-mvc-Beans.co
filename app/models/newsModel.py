from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class News(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    konten = db.Column(db.String(100), nullable=False)
    imaage = db.Column(db.String(100), nullable=False)

    def __init__(self, title, konten, imaage):
        self.title = title
        self.konten = konten
        self.imaage = imaage
