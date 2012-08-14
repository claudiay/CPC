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
    common_name = db.Column(db.String(50), nullable = False)
    plant_type = db.Column(db.String(10), nullable = False)
    scientific_name = db.Column(db.String(50), nullable = True)
    helps = db.Column(db.String(500), nullable=True)
    helped_by = db.Column(db.String(500), nullable=True)
    attracts = db.Column(db.String(500), nullable=True)
    repels = db.Column(db.String(500), nullable=True)
    avoid = db.Column(db.String(500), nullable=True)
    comment = db.Column(db.String(700), nullable=True)

    def __init__(self, common_name, plant_type, scientific_name, helps,
       		helped_by, attracts, repels, avoid, comment):
	self.common_name = common_name
	self.plant_type = plant_type
	self.scientific_name = scientific_name
	self.helps = json.dumps(helps)
	self.helped_by = json.dumps(helped_by)
	self.attracts = json.dumps(attracts)
	self.repels = json.dumps(repels)
	self.avoid = json.dumps(avoid)
	self.comment = comment

    @property
    def serialize(self):
        return {'id': self.id,
                'name': self.common_name,
                'science': self.scientific_name,
                }

# "zip code", "state abbreviation", "latitude", "longitude", "city", "state"
class Location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    zipcode = db.Column(db.String(15), nullable = False)
    state_abbrevation = db.Column(db.String(2), nullable = False)
    latitude = db.Column(db.String(15), nullable = False)
    longitude = db.Column(db.String(15), nullable = False)
    city = db.Column(db.String(30), nullable = True)
    state = db.Column(db.String(30), nullable = False)

    def __init__(self, zipcode, state_abbrevation, latitude,
    		longitude, city, state):
        self.zipcode = zipcode
	self.state_abbrevation = state_abbrevation
	self.latitude = latitude
	self.longitude = longitude
	self.city = city
	self.state = state

