from math import pi, sin, cos
from turtle import pen, up, down, setposition, setheading, circle, clear, hideturtle


def polar_coord_to_cartesian(angle, radius):
    x_coord = radius * cos(angle)
    y_coord = radius * sin(angle)
    return (x_coord, y_coord)


def get_node_angle(node, mod):
    return (node * 2 * pi) / mod


def get_coord_of_node(node, mod, radius):
    angle = get_node_angle(node, mod)
    coord = polar_coord_to_cartesian(angle, radius)
    return coord


def reset_cursor(*coord):
    up()
    setposition(*coord)
    down()


def reset_canvas(radius):
    reset_cursor(*polar_coord_to_cartesian(0, radius))
    setheading(90)
    clear()
    circle(radius)


def main():
    radius = 200
    pen(speed=1000, pensize=2)
    hideturtle()
    cont = "continue"
    while "q" not in cont:
        mod = int(input("Modulo: "))
        multiplier = int(input("Multiplier: "))
        reset_canvas(radius)
        for node in range(mod):
            start = get_coord_of_node(node, mod, radius)
            end = get_coord_of_node(node*multiplier, mod, radius)
            reset_cursor(*start)
            setposition(*end)
        cont = input("q to quit: ")


if __name__ == '__main__':
    main()
