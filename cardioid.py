from math import pi, sin, cos
from turtle import pen, penup, pendown, setposition, setheading, circle, clear, hideturtle
from contextlib import contextmanager


def polar_coord_to_cartesian(angle, radius):
    """
    take a angle and a radius (polar coordinate)
    return x and y coordinates (cartesian coordinate)
    """
    x_coord = radius * cos(angle)
    y_coord = radius * sin(angle)
    return (x_coord, y_coord)


def get_node_angle(node, mod):
    """node index to an angle"""
    return (node * 2 * pi) / mod


def get_coord_of_node(node, mod, radius):
    """from a node index, generate the corresponding coordinate"""
    angle = get_node_angle(node, mod)
    coord = polar_coord_to_cartesian(angle, radius)
    return coord


@contextmanager
def draw():
    """engage the pen, draw something, and dis-engage the pen when your done"""
    pendown()
    yield
    penup()


def main():
    """main program execution"""
    radius = 200 # radius of circle
    pen(speed=1000, pensize=2) # initialise pen
    penup() # disengage the pen
    hideturtle() # hide the cursor
    cont = "continue"
    while "q" not in cont:
        setposition(*polar_coord_to_cartesian(0, radius))
        setheading(90) # put cursor in start position
        with draw():
            circle(radius) # draw bounding circle
        mod = int(input("Modulo: ")) # read from user the number of marks to put around the circle
        multiplier = float(input("Multiplier: ")) # read the value to be used as a multiplier
        for node in range(mod): # loop through each mark
            start = get_coord_of_node(node, mod, radius)
            end = get_coord_of_node(node*multiplier, mod, radius)
            setposition(*start) # put the cursor on the mark
            with draw():
                setposition(*end) # draw line to the destination
        cont = input("q to quit: ") # do they want to go again?
        clear() # clear drawing to make room for the next one


if __name__ == '__main__':
    main()
    
