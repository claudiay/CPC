#!/usr/bin/env python
from flask import Flask, jsonify, redirect, url_for, render_template, request, g
import setplants
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
from grid import generate_squares
from model import Location, Plants, db
import json

app = Flask(__name__)

# Front page
# Asks for zipcode, season, and plot size 
@app.route("/")
def home():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    return render_template('/index.html', seasons=seasons)

# Step 1
# Asks user to select plants.
@app.route("/select_plants", methods=["GET"])
def info():
    zipcode = request.args['zip_code']
    season = request.args['season_id']
    width = int(request.args['plot-width'])
    length = int(request.args['plot-length'])
    location = db.session.query(Location).filter(Location.zipcode == zipcode).one()
    state = location.state
    city = location.city
    latitude = location.latitude
    longitude = location.longitude
    plant_list = db.session.query(Plants).all()
    json_plants = [ plant.serialize for plant in plant_list ]
    list_len = int(len(plant_list)/2)
    g.json = json
    return render_template('/select_plants.html', season=season,
			width=width, length=length, state=state,
			city=city, plant_list=json_plants,
			list_len=list_len, longitude=longitude,
			latitude=latitude)

# Step 1.2
# Generates list of plants, caps the list at the size of the plot.
@app.route("/list", methods=["GET"])
def modify_list():
    size = int(request.args['size'])
    return render_template('/list.html', size=size)


# Generates plots and plants, for user to place any pre-planned plants
@app.route("/plots", methods=["POST"])
def create_plot():
    width = int(request.form['width'])
    length = int(request.form['length'])
    squares = generate_squares(width, length)
    plot_width = width * 117
    plant_width = 350
    if len(squares) > 20:
        plant_width = 500
    return render_template('/plots.html', squares=squares, plot_width=plot_width,
    			plant_width=plant_width)

# Returns Optimal Garden layout
@app.route('/fin')
def show_plot():
    picked_plants = 0
    guide = {} 
    for plant in picked_plants:
        # request info from database and add to guide
	guide[plant] = "info"
    # run setplants.py and return as garden_layout
    return True # Return garden_layout hash table

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")