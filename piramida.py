import turtle
from turtle import *
a = 7
turtle.speed(10)

def rysuj_puzzle():
    pendown()
    setheading(90)
    turtle.fillcolor("orange")
    turtle.begin_fill()
    i=1
    while i<5:
        turtle.forward(2*a)
        rt(90)
        turtle.forward(a)
        lt(90)
        turtle.forward(a)
        lt(90)
        turtle.forward(a)
        rt(90)
        turtle.forward(2 * a)
        rt(90)
        i=i+1
    penup()

    turtle.end_fill()

def rysuj_piramide(liczba_klockow):

    i=1
    while i<=liczba_klockow:
        j = 1
        while j <= i:
          goto((i-1)*6*a,(j-1)*6*a)
          rysuj_puzzle()
          j = j + 1

        i=i+1


rysuj_piramide(4)

turtle.mainloop()