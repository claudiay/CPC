"""
This program creates new databases for all tables included in model.py.
"""
import json, model
from model import Plants, Location

def upload_locations(file):
    f = open(file)
    for line in f:
        l = line.strip().replace(' " ', "").replace(' "', "").replace('"', "").split(",")
        print l
        location = Location(*l)
        model.add(location)
        model.save_all()

def upload_plants(plant_data_file):
    # Grab the json string from data.txt
    f = open(plant_data_file, 'r')
    io = f.read()
    plant_dict = json.loads(io)
    f.close()
    
    # Upload plants into the database
    dict_type = ['veg', 'flo', 'her']
    for _dict in dict_type:
    	p_dict = plant_dict[_dict]
	for key in p_dict:
	    entry = [key, p_dict[key]["plant_type"], p_dict[key]["scientific_name"],
	    	p_dict[key]["helps"], p_dict[key]["helped_by"], p_dict[key]["attracts"],
		p_dict[key]["repels"], p_dict[key]["avoid"], p_dict[key]["comment"]]
            print entry
	    plant = Plants(*entry)
	    model.add(plant)
    	    model.save_all()

def check():
    print "Are you sure you want to create all new updated databased?"
    print "Make sure that you get rid of and clear the old databased."
    print "type 'yes', otherwise, program will quit"
    check = raw_input(">> ")
    if check == "yes":
        return True
    else:
        return False

def main():
    run = check()
    if run == True:
        model.db.create_all()
	upload_locations("plantdata/zips.csv")
	upload_plants('plantdata/data.txt')


if __name__ == '__main__':
    main()
