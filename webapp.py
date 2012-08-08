#!/usr/bin/env python
from flask import Flask, jsonify, redirect, url_for, render_template, request
import setplants
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
from grid import generate_squares
from model import Location, db

app = Flask(__name__)

@app.route("/")
def home():
    states = db.session.query(distinct(Location.state))
    cities = []
    picked_state = "California"
    for entry in db.session.query(Location).filter(Location.state == picked_state):
        city = entry.city
	if len(city) > 1:
	    if city not in cities:
	        cities.append(city)
    seasons = ['spring', 'summer', 'fall', 'winter']
    squares = generate_squares(3, 3)
    return render_template('/index.html', cities=sorted(cities), states=states, 
    			seasons=seasons, squares=squares)

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
