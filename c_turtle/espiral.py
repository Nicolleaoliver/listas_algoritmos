import turtle
import math

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    theta = 0.0
    for i in range(n):
        t.fd(length)
    
        d_theta = 1 / (a + b * theta)
        t.lt(d_theta)
        theta += d_theta

screen = turtle.Screen()
bob = turtle.Turtle()
bob.speed(0)     
bob.pensize(2)   

draw_spiral(bob, n=1000)

turtle.done()