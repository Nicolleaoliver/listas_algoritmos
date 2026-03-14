import turtle
import math

def desenhar_fatia(t, r, angle):
    angulo_base = (180 - angle) / 2
    borda = 2 * r * math.sin(math.radians(angle / 2))
    
    t.fd(r)
    t.lt(180 - angulo_base)
    t.fd(borda)
    t.lt(180 - angulo_base)
    t.fd(r)

def desenhar_torta(t, n, r):
    angle = 360 / n
    for i in range(n):
        desenhar_fatia(t, r, angle)
        t.lt(angle)

bob = turtle.Turtle()
bob.speed(0)
desenhar_torta(bob, 6, 100)

turtle.done()