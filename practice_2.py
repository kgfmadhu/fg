from turtle import Turtle,Screen
import random
t=Turtle()
s=Screen()
l=["red","blue","green","yellow","grey","violet","brown","black"]

def draw(no_of_sides):
    angle=360/no_of_sides
    for i in range(no_of_sides):
        t.forward(100)
        t.right(angle)


for i in range(4,9):
    t.color(random.choice(l))
    draw(i)
s.exitonclick()



