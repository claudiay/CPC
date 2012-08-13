#!/usr/bin/env python
# Returns a dictionary of plant placement on the graph.
from grid import generate_squares, generate_peers

def parse_grid(squares, picked_plants):
    """Convert grid to a dict of possible values {square:[avaliable plants]}"""
    # To start, every square can be any plant,
    # then assign values from the grid, if any. (add feature later)
    return dict((s, picked_plants) for s in squares)

def prepicked_values(grid, squares):
    """Convert grid into a dict of {square:char} with "." for empty."""
    # This is needed for the added feature in parse_grid.
    # Not currently in use.
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

def square_benefit(values, plant, square, guide, peers):
    """Returns benefit of placing the plant in that square."""
    score = 0
    plant = plant[:-1]
    square_peers = peers[square]

    # Check benefit/cost for assigned squares.
    for peer in square_peers:
        if len(values[peer]) == 1: # if assigned
	    if values[peer][0][:-1] in guide[plant]['avoid']:
	        score = score - 5
	    elif values[peer][0][:-1] in guide[plant]['friend']:
	        score = score + 3
	    elif values[peer][0][:-1] == plant:
	        score = score - 1
    return score

def solve(guide, squares, picked_plants, peers):
    values = parse_grid(squares, picked_plants)
    if all(len(values[s]) == 1 for s in squares):
        return values # Fin!
    for square in values:
        benefit, picked = max((square_benefit(values, p, square, guide, peers), p) 
		for p in picked_plants)
	print "for %s, place %s, with benefit: %s" %(square, picked, benefit)
	assign(values, square, picked)
    return values


def main():
    peers = generate_peers(3,3)
    squares = generate_squares(3,3)
    picked_plants = ['corn1', 'corn2', 'tomato1', 'tomato2', 'tomato3', 
    		     'strawberry1', 'strawberry2', 'strawberry3', 'potato1']
    guide = {'corn': 
    		{'friend':['tomato'], 'avoid':['potato']},
    	     'tomato':
	     	{'friend':['strawberry'], 'avoid':['potato']},
	     'strawberry':
	     	{'friend':['tomato'], 'avoid':[]},
	     'potato':
	     	{'friend':[], 'avoid':['corn']}
	    }
    print solve(guide, squares, picked_plants, peers)



if __name__ == '__main__':
    main()
