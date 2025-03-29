import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///countries.db'  # SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

