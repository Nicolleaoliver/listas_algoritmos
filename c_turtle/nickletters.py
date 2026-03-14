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

def move(t, distance):
    t.pu()
    t.fd(distance)
    t.pd()


def draw_n(t, h):
    angle = math.degrees(math.atan(h / (h/2))) 
    dist = math.sqrt(h**2 + (h/2)**2)          
    
    t.lt(90)
    t.fd(h)    
    t.rt(180 - (90 - angle))
    t.fd(dist)  
    t.lt(180 - (90 - angle))
    t.fd(h)     
    t.rt(180)
    t.fd(h)     
    t.lt(90)

def draw_i(t, h):
    t.lt(90)
    t.fd(h)
    t.bk(h)
    t.rt(90)

def draw_c(t, h):
    r = h / 2
    t.pu()
    t.fd(r)     
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.pd()
    arc(t, r, 180) 
    t.pu()
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(r)
    t.pd()

def draw_k(t, h):
    largura = h * 0.5
    t.lt(90)
    t.fd(h)      
    t.bk(h/2)   
    t.rt(45)
    t.fd(h/1.4)  
    t.bk(h/1.4)
    t.rt(90)
    t.fd(h/1.4) 

    t.pu()
    t.lt(135)    
    t.bk(h/2)    
    t.fd(largura + 10) 
    t.pd()


bob = turtle.Turtle()
bob.speed(3)
bob.pensize(3) 


draw_n(bob, 100)
move(bob, 40)

draw_i(bob, 100)
move(bob, 40)

draw_c(bob, 100)
move(bob, 60)

draw_k(bob, 100)

turtle.done()