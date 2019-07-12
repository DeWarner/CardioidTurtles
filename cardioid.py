from math import pi, sin, cos
from turtle import pen, up, down, setposition, setheading, circle, clear, hideturtle


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


def reset_cursor(coord, heading=None):
    """move the cursor to the provided coordinate without drawing"""
    up() # lift pen off canvas
    setposition(*coord) # move pen
    if heading is not None:
        setheading(heading) # orient the pen
    down() # re-engage the pen


def main():
    """main program execution"""
    radius = 200 # radius of circle
    pen(speed=1000, pensize=2) # initialise pen
    hideturtle() # hide the cursor
    cont = "continue"
    while "q" not in cont:
        reset_cursor(polar_coord_to_cartesian(0, radius), 90) # put cursor in start position
        circle(radius) # draw bounding circle
        mod = int(input("Modulo: ")) # read from user the number of marks to put around the circle
        multiplier = num(input("Multiplier: ")) # read the value to be used as a multiplier
        for node in range(mod): # loop through each mark
            start = get_coord_of_node(node, mod, radius)
            end = get_coord_of_node(node*multiplier, mod, radius)
            reset_cursor(start) # put the cursor on the mark
            setposition(*end) # draw line to the destination
        cont = input("q to quit: ") # do they want to go again?
        clear() # clear drawing to make room for the next one


if __name__ == '__main__':
    main()
    
