import turtle
from turtle import *
a = 100

def rysuj_kwadrat():
    pendown()
    setheading(90)
    i=1
    while i<5:
        turtle.forward(a)
        rt(90)
        i=i+1
    penup()


rysuj_kwadrat()


turtle.mainloop()