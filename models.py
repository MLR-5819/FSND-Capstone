import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

#Sets database path from setup.sh for app deployment
database_path = os.environ.get('DATABASE_URL')

#Sets database path during local usage
if not database_path:
    database_name = "thisorthat"
    database_path = "postgres://{}:{}@{}/{}".format('postgres', 'password', 'localhost:5432', database_name)

db = SQLAlchemy()

#Setup db to bind flask app with SQLAlchemy service
def setup_db(app, database_path = database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#Setup tables in database
class Entry(db.Model):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True) 
    name = Column(String)
    category = Column(String)
    entry_url = Column(String)
    votes = Column(Integer)
    date = 

    def __init__(self, name, category, entry_url, votes, date):
        self.name = name
        self.category = category
        self.entry_url = entry_url
        self.votes = votes
        self.date = date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'entry_url': self.entry_url,
            'votes': self.votes
        }


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }
