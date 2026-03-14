import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def skip(t, length):
    t.pu()
    t.fd(length)
    t.pd()


def draw_a(t, height):
    angle = 75
    hyp = height / math.sin(math.radians(angle))
    t.lt(angle)
    t.fd(hyp)
    t.rt(2 * angle)
    t.fd(hyp)
    t.pu()
    t.bk(hyp/2)
    t.pd()
    t.rt(180 - angle)
    t.fd(hyp/2) 
    
    t.pu()
    t.lt(90)
    t.fd(height/2)
    t.lt(90)
    t.fd(height/4)
    t.pd()

def draw_b(t, height):
    r = height / 4
    t.lt(90)
    t.fd(height)
    t.rt(90)
    arc(t, r, 180)
    t.rt(180)
    arc(t, r, 180)
    t.pu()
    t.home() 
    t.pd()

def draw_c(t, height):
    r = height / 2
    t.pu()
    t.fd(r)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.pd()
    arc(t, r, 180)


def main():
    screen = turtle.Screen()
    bob = turtle.Turtle()
    bob.speed(3)

    draw_a(bob, 100)
    skip(bob, 50)
    draw_b(bob, 100)
    skip(bob, 120)
    draw_c(bob, 100)

    turtle.done()

if __name__ == "__main__":
    main()