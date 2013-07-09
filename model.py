#!/usr/bin/env python
import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plantdata.db'
db = SQLAlchemy(app)

def add(item):
    db.session.add(item)

def save_all():
    db.session.commit()

# common_name, plant_type, scientific_name, helps, helped_by, 
# attracts, repels, avoid, comment
class Plants(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    friend = db.Column(db.String(500), nullable=True)
    avoid = db.Column(db.String(500), nullable=True)

    def __init__(self, name, friend, avoid):
	self.name = name
	self.friend = json.dumps(friend)
	self.avoid = json.dumps(avoid)

    @property
    def serialize(self):
        return {'id': self.id,
                'name': self.name,
                }

