import turtle as t
import random as r
tim=t.Turtle()
screen=t.Screen()
l=[0,90,270,180]
def set_color():
    red=r.randint(0,200)
    green=r.randint(0,200)
    blue=r.randint(0,200)
    rgb=(red,green,blue)
    return rgb

def rand_walk():
    for i in range(200):
        tim.forward(20)
        tim.setheading(r.choice(l))
        tim.color(set_color())
tim.width(10)
tim.speed(10000)
rand_walk()

screen.exitonclick()