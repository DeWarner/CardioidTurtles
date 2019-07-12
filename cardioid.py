from math import pi, sin, cos
from turtle import pen, up, down, setposition, setheading, circle, clear

def get_point_from_angle(angle, scale):
    return (scale*cos(angle), scale*sin(angle))

def angle_from_point(point, mod):
    return (2*point*pi/mod)

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
        setposition(get_point_from_angle(0, scale))
        down()
        circle(scale)
        for point in range(mod):
            up()
            angle = angle_from_point(point,mod)
            next_angle = angle_from_point(point*multiplier, mod)
            start = get_point_from_angle(angle, scale)
            end = get_point_from_angle(next_angle, scale)
            setposition(*start)
            down()
            setposition(*end)
    
        cont = input("q to quit: ")


if __name__ == '__main__':
    main()
