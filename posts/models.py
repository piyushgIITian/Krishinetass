from flask import request,render_template
from utils import app


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Posts(db.Model):
    __tablename__ = 'posts'
    message = db.Column(db.String(40),primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __init__(self,message,lat,lon):
        self.message = "{"+message+"}"
        self.lat = lat
        self.lon = lon
