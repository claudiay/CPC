#!/usr/bin/env python
# Returns a dictionary of plant placement on the graph.
from grid import generate_squares, generate_peers
from itertools import permutations
from copy import deepcopy

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

def set_plants(squares, picked_plants):
    picked_plants = list(picked_plants)
    return {squares[i]:[picked_plants[i]] for i in range(len(squares))}

def score(squares, picked_plants, peers, guide):
    current = set_plants(squares, picked_plants)
    benefits = {}
    
    for square in current:
        plant = current[square][0]
        benefits[square] = square_benefit(current, plant, square, guide, peers)   
    
    total = sum(benefits.itervalues())
    return total, picked_plants, benefits

def solve(guide, picked_plants, width, length):
    """Iterates through all possible ordering of the plants.
    Compares the benefits of each setting of plants, and returns the highest
    score."""

    peers = generate_peers(width, length)
    squares = generate_squares(width, length)
    
    patterns = {plants:True 
            for plants in permutations(picked_plants, len(picked_plants))}
    
    planting_score, best_values, best_benefits = max(
            score(squares, plants, peers, guide) for plants in patterns)
    
    return set_plants(squares, best_values), best_benefits


