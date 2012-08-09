#!/usr/bin/env python
from flask import Flask, jsonify, redirect, url_for, render_template, request
import setplants
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
from grid import generate_squares
from model import Location, db

app = Flask(__name__)

# Front page
@app.route("/")
def home():
    return render_template('/index.html')

# Step 1
# Asks for state, city, season, plot size, and plants. 
@app.route("/info.html")
def info():
    states = db.session.query(distinct(Location.state))
    seasons = ['spring', 'summer', 'fall', 'winter']
    return render_template('/info.html', states=states, seasons=seasons)

# Generates cities to select, based on selected state.
@app.route("/get_cities", methods=["GET"])
def generate_cities():
    state = request.args['state_id']
    cities = []
    for entry in db.session.query(Location).filter(Location.state == state):
        city = entry.city
        if len(city) > 1:
            if city not in cities:
	        cities.append(city)
    return jsonify(cities=sorted(cities))

# Step 2
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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
