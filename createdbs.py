#!/usr/bin/env python
"""
This program creates new databases for all tables included in model.py.
"""
import json, model
from model import Plants

def upload_plants(file_name):
    # Grab the json string from data.txt
    f = open(file_name)
    for line in f:
        line = line.strip()
        info = line.split("|")
        entry = [info[0], info[1].split(","), info[2].split(",")]
        print entry
        plant = Plants(*entry)
        model.add(plant)
        model.save_all()
    f.close()
        

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
	upload_plants('plantdata/newdata.txt')


if __name__ == '__main__':
    main()
