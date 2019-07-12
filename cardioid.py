from math import pi, sin, cos
from turtle import pen, up, down, setposition, setheading, circle, clear

def polar_coord_to_cartesian(angle, radius):
    return (radius*cos(angle), radius*sin(angle))

def get_node_angle(node, mod):
    return (2*node*pi/mod)

def get_coord_of_node(node, mod, radius):
    angle = get_node_angle(node, mod)
    coord = polar_coord_to_cartesian(angle, radius)

def main():
    pen(speed=1000, pensize=2)
    cont = "continue"
    while "q" not in cont:
        clear()
        radius = 200
        mod = int(input("Modulo: "))
        multiplier = int(input("Multiplier: "))
        setheading(90)
        up()
        setposition(*polar_coord_to_cartesian(0, radius))
        down()
        circle(radius)
        for node in range(mod):
            up()
            start = get_coord_of_node(node, mod, radius)
            end = get_coord_of_node(node*multiplier, mod, radius)
            setposition(*start)
            down()
            setposition(*end)
    
        cont = input("q to quit: ")


if __name__ == '__main__':
    main()
