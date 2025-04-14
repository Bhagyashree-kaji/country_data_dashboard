from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    capital = db.Column(db.String(100))
    region = db.Column(db.String(50))
    population = db.Column(db.BigInteger)
    flag_url = db.Column(db.String(300))







