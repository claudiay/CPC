#!/usr/bin/env python
# Returns a dictionary of plant placement on the graph.
from grid import generate_squares, generate_peers

def image_list():
    f = open("plantdata/images.txt")
    return [p.strip() for p in f]

def create_grid(squares, picked_plants):
    """Convert grid to a dict of possible values {square:[avaliable plants]}"""
    return dict((s, picked_plants) for s in squares)

# Add this feature later
def prepicked_values(grid, squares):
    """Convert grid into a dict of {square:char} with "." for empty."""
    pass

def assign(values, square, plant):
    """Eliminates all other values besides plant from square.
    Elminates plant from all other squares."""
    values[square]=[plant] # assign plant to plot
    for plot in values:
        # remove plant from all other plots
        if plot != square and values[plot].count(plant) >= 1:
	    i = values[plot].index(plant) 
	    values[plot].pop(i) # removed assigned plant from list
    return values

def remove_nums(word):
    letters = []
    for c in word:
        if c.isdigit() == False:
            letters.append(c)
    return ''.join(letters)

def square_benefit(values, plant, square, guide, peers):
    """Returns benefit of placing the plant in that square."""
    score = 0
    plant = remove_nums(plant)
    square_peers = peers[square]
    # Check benefit/cost for assigned squares.
    for peer in square_peers:
        if len(values[peer]) == 1: # if assigned
            peer_plant = remove_nums(values[peer][0])
            if peer_plant in guide[plant]['avoid']:
	        score = score - 5
	    elif peer_plant in guide[plant]['friend']:
	        score = score + 3
	    elif peer_plant == plant:
	        score = score - 1
    return score

def clean_dict(values):
    for square in values:
        clean = remove_nums(values[square][0])
        values[square][0] = clean
    return values

def solve(guide, picked_plants, width, length):
    peers = generate_peers(width, length)
    squares = generate_squares(width, length)
    values = create_grid(squares, picked_plants)
    benefits = {}
    for square in values:
        # Find max beneficial plant for each square.
        benefit, picked = max((square_benefit(values, p, square, guide, peers), p) 
		for p in values[square])
        assign(values, square, picked)
    for square in values:
        plant = values[square][0]
        benefits[square] = square_benefit(values, plant, square, guide, peers)   
    clean_dict(values)
    return values, benefits


