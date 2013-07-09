#!/usr/bin/env python
from flask import Flask, jsonify, redirect, url_for, render_template, request, g
import setplants, json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
from grid import generate_squares
from model import Plants, db

app = Flask(__name__)

# Front page
# Asks for zipcode, season, and plot size 
@app.route("/")
def home():
    return render_template('/index.html')

# Step 1
# Asks user to select plants.
@app.route("/select_plants", methods=["GET"])
def info():
    width = int(request.args['plot-width'])
    length = int(request.args['plot-length'])
    plant_list = db.session.query(Plants).all()
    json_plants = [ plant.serialize for plant in plant_list ]
    list_len = int(len(plant_list)/2)
    g.json = json
    return render_template('/select_plants.html',
			    width=width, length=length, plant_list=json_plants,
			    list_len=list_len)

# Returns Optimal Garden layout
@app.route('/fin', methods=['POST'])
def show_plot():
    image_list = setplants.image_list()
    plant_count = json.loads(request.form.get('plant_counts'))
    length = int(json.loads(request.form.get('plot_length')))
    width = int(json.loads(request.form.get('plot_width')))
    guide = {}
    picked_plants = []
    for key in plant_count:
        if plant_count[key] > 0:
            print plant_count[key]
            for i in range(plant_count[key]):
                plant = db.session.query(Plants).get(int(key))
                picked_plants.append(plant.name+str(i))
                guide[plant.name] = {'friend':plant.friend,
                                            'avoid':plant.avoid}
    solved, benefits = setplants.solve(guide, picked_plants,
                                        width, length)
    print solved, benefits
    order = generate_squares(width, length)
    total_score = sum(benefits[p] for p in benefits)
    return render_template('/fin.html', order=order,
            solved=solved, benefits=benefits, image_list=image_list,
            length=length, width=width, box=111, total_score=total_score)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
