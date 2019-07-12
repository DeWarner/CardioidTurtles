from math import pi, sin, cos
from turtle import pen, up, down, setposition, setheading, circle, clear

def get_coord_from_angle(angle, scale):
    return (scale*cos(angle), scale*sin(angle))

def get_node_angle(node, mod):
    return (2*node*pi/mod)

def main():
    pen(speed=1000, pensize=2)
    cont = "continue"
    while "q" not in cont:
        clear()
        scale = 200
        mod = int(input("Modulo: "))
        multiplier = int(input("Multiplier: "))
        setheading(90)
        up()
        setposition(get_coord_from_angle(0, scale))
        down()
        circle(scale)
        for node in range(mod):
            up()
            angle = get_node_angle(node,mod)
            next_angle = get_node_angle(node*multiplier, mod)
            start = get_coord_from_angle(angle, scale)
            end = get_coord_from_angle(next_angle, scale)
            setposition(*start)
            down()
            setposition(*end)
    
        cont = input("q to quit: ")


if __name__ == '__main__':
    main()
