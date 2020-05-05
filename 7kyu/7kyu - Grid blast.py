# 7kyu - Grid blast!

""" Ready! Set! Fire... but where should you fire?

The battlefield is 3x3 wide grid. HQ has already provided you with an array for easier computing.

HQ radios you with 'x' and 'y' coordinates. x=0 y=0 being 'top left' part of the battlefield;

Your duty is to create a function that takes those Xs and Ys and return the correct grid sector to be hit.

fire(0,0) # 'top left'
fire(1,2) # 'bottom middle'

Notice the grid is a monodimensional array """

grid = ['top left',    'top middle',    'top right',
        'middle left', 'center',        'middle right',
        'bottom left', 'bottom middle', 'bottom right']


def fire(x, y):
    return grid[x + 3 * y]


q = fire(0, 0), "top left"
q
q = fire(1, 1), "center"
q
