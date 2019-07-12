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
    up()
    setposition(*coord)
    if heading is not None:
        setheading(heading)
    down()


def main():
    """main program execution"""
    radius = 200
    pen(speed=1000, pensize=2)
    hideturtle()
    cont = "continue"
    while "q" not in cont:
        reset_cursor(polar_coord_to_cartesian(0, radius), 90)
        clear()
        circle(radius)
        mod = int(input("Modulo: "))
        multiplier = int(input("Multiplier: "))
        for node in range(mod):
            start = get_coord_of_node(node, mod, radius)
            end = get_coord_of_node(node*multiplier, mod, radius)
            reset_cursor(start)
            setposition(*end)
        cont = input("q to quit: ")


if __name__ == '__main__':
    main()
    
