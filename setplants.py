#!/usr/bin/env python
"""
Returns a dictionary of plant placement on the graph.
"""
from grid import generate_squares, generate_peers

def parse_grid(squares, picked_plants):
    """Convert grid to a dict of possible values {square:[avaliable plants]}"""
    # To start, every square can be any plant,
    # then assign values from the grid, if any. (add feature later)
    return dict((s, picked_plants) for s in squares)

def grid_values(grid, squares):
    """Convert grid into a dict of {square:char} with "." for empty."""
    # This is needed for the added feature in parse_grid.
    # Not currently in use.
    pass

def assign(values, square, plant):
    """Eliminates all other values besides plant from square.
    Elminates plant from all other squares."""
    values[square]=[plant]
    for plot in values:
        if plot != square:
	    print plot
	    if values[plot].count(plant) >= 1:
	        i = values[plot].index(plant)
		print i
		values[plot].pop(i)
		print values[plot]
    return values

def main():
    peers = generate_peers(3,3)
    squares = generate_squares(3,3)
    picked_plants = ['corn1', 'corn2', 'tomato1', 'tomato2', 'tomato3', 
    		     'strawberry1', 'strawberry2', 'strawberry3', 'potato1']
    guide = {'corn': 
    		{'friend':['tomato'], 'avoid':['potato', 'corn']},
    	     'tomato':
	     	{'friend':['strawberry'], 'avoid':['potato', 'tomato']},
	     'strawberry':
	     	{'friend':['tomato'], 'avoid':['strawberry']},
	     'potato':
	     	{'friend':[], 'avoid':['corn', 'potato']}
	    }
    values = parse_grid(squares, picked_plants)
    print assign(values, "A1", "corn1")
    print assign(values, "B1", "corn2")



if __name__ == '__main__':
    main()
