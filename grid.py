#!/usr/bin/env python
"""
Returns the optimal garden plan for selected plants.
"""

def generate_squares(width,length):
    """Generates a grid with unique character points.
    Max width is 9, max length is 24."""
    cols = "123456789"
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = cols[:width]
    rows = rows[:length]

    return [row+col for row in rows for col in cols]


def generate_peers(width,length):
    """Generates a dict of peers for each unique character point. 
    Max width is 9, max length is 24."""
    
    cols = "123456789"
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = cols[:width]
    rows = rows[:length]
    grid = []
    for row in rows:
        grid.append([row+col for col in cols])
    peers = dict((plot, find_peers(plot, grid)) 
    		for plot in [r+c for r in rows for c in cols])
    return peers

def find_peers(plot, grid):
    """Returns a list of a plot's peers.
    Top, left, right, bottom."""

    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_row = rows.find(plot[0])
    current_col = int(plot[1])
    # Find the peers on the top
    if current_row == 0:
        top = []
    elif current_col == 1:
        top = grid[current_row-1][:current_col+1]
    else:
        top = grid[current_row-1][current_col-2:current_col+1]
    # Find peers on the sides, left then right. 
    if current_col == 1:
        sidel = []
    else:
        sidel = [grid[current_row][current_col-2]]
    if current_col == len(grid[0]):
        sider = []
    else:
        sider = [grid[current_row][current_col]]
    # Find peers on the bottom
    if current_row == len(grid)-1:
        bottom = []
    elif current_col == 1:
    	bottom = grid[current_row+1][:current_col+1]
    else:
        bottom = grid[current_row+1][current_col-2:current_col+1]
    return top + sidel + sider + bottom

if __name__ == '__main__':
    main()
